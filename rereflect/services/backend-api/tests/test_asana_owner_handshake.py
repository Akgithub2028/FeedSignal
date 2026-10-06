"""Provider registration must permit the initial callback before returning."""
import asyncio

import httpx
import pytest
from cryptography.fernet import Fernet
from fastapi import HTTPException, Request, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base, Organization
from src.models.asana_integration import AsanaIntegration
from src.api.routes import asana_integration, asana_webhook
from src.services.asana_client import AsanaClient, AsanaTransientError
from src.utils.encryption import decrypt_api_key, encrypt_api_key


@pytest.fixture
def sessions(tmp_path, monkeypatch):
    monkeypatch.setenv('LLM_ENCRYPTION_KEY', Fernet.generate_key().decode())
    engine = create_engine(f'sqlite:///{tmp_path / "asana.sqlite"}')
    Base.metadata.create_all(engine, tables=[Organization.__table__, AsanaIntegration.__table__])
    factory = sessionmaker(bind=engine)
    with factory() as db:
        db.add(Organization(id=1, name='Owner'))
        db.flush()
        db.add(AsanaIntegration(organization_id=1, api_token=encrypt_api_key('test-pat'),
            is_active=True, webhook_gid='old-hook', webhook_url_token='old-url',
            webhook_secret=encrypt_api_key('old-secret')))
        db.commit()
    yield factory
    engine.dispose()


def test_callback_can_resolve_committed_token_before_provider_returns(sessions, monkeypatch):
    class Provider:
        def create_webhook(self, resource_gid, target_url):
            with sessions() as callback_db:
                response = Response()
                request = Request({'type':'http', 'headers':[(b'x-hook-secret', b'new-secret')]})
                asyncio.run(asana_webhook.asana_webhook_inbound(
                    target_url.rsplit('/',1)[1], request, response, callback_db))
                assert response.headers['X-Hook-Secret'] == 'new-secret'
            return {'gid':'new-hook'}
        def close(self): pass
    monkeypatch.setattr(asana_integration, 'AsanaClient', lambda token: Provider())
    with sessions() as db:
        result = asana_integration.asana_webhook_enable(
            asana_integration.AsanaWebhookEnableRequest(resource_gid='project'), Organization(id=1), db)
        db.expire_all()
        row = db.query(AsanaIntegration).one()
        assert result.webhook_gid == row.webhook_gid == 'new-hook'
        assert decrypt_api_key(row.webhook_secret) == 'new-secret'
        assert row.webhook_url_token != 'old-url'


def test_failed_registration_restores_previous_verified_callback(sessions, monkeypatch):
    class Provider:
        def create_webhook(self, resource_gid, target_url):
            with sessions() as callback_db:
                row = callback_db.query(AsanaIntegration).one()
                assert row.webhook_url_token == target_url.rsplit('/',1)[1]
                assert row.webhook_secret is None
            raise AsanaTransientError('provider unavailable')
        def close(self): pass
    monkeypatch.setattr(asana_integration, 'AsanaClient', lambda token: Provider())
    with sessions() as db:
        with pytest.raises(HTTPException) as error:
            asana_integration.asana_webhook_enable(
                asana_integration.AsanaWebhookEnableRequest(resource_gid='project'), Organization(id=1), db)
        assert error.value.status_code == 502
        db.expire_all()
        row = db.query(AsanaIntegration).one()
        assert row.webhook_gid == 'old-hook'
        assert row.webhook_url_token == 'old-url'
        assert decrypt_api_key(row.webhook_secret) == 'old-secret'


def test_provider_rejection_is_a_sanitized_registration_error(monkeypatch):
    real = httpx.Client
    def reject(request):
        return httpx.Response(400, json={'errors':[{'message':'private provider details'}]})
    monkeypatch.setattr('src.services.asana_client.httpx.Client',
        lambda **kwargs: real(transport=httpx.MockTransport(reject), **kwargs))
    with AsanaClient('test-pat') as client:
        with pytest.raises(AsanaTransientError) as error:
            client.create_webhook('project', 'https://example.com/private-callback')
    assert 'private provider details' not in str(error.value)
    assert 'private-callback' not in str(error.value)


@pytest.mark.parametrize('content', ['invalid-json', '{"data":[]}', '{"data":{}}', '{"data":{"gid":""}}'])
def test_malformed_provider_success_uses_registration_error(monkeypatch, content):
    real=httpx.Client
    monkeypatch.setattr('src.services.asana_client.httpx.Client', lambda **kwargs:
        real(transport=httpx.MockTransport(lambda request: httpx.Response(200, text=content)), **kwargs))
    with AsanaClient('test-pat') as client:
        with pytest.raises(AsanaTransientError):
            client.create_webhook('project', 'https://example.com/private-callback')


def test_overlapping_registration_is_rejected_and_failure_preserves_original(sessions, monkeypatch):
    class Provider:
        calls = 0
        def create_webhook(self, resource_gid, target_url):
            Provider.calls += 1
            assert Provider.calls == 1, 'overlapping registration reached the provider'
            with sessions() as competing_db:
                with pytest.raises(HTTPException) as overlap:
                    asana_integration.asana_webhook_enable(
                        asana_integration.AsanaWebhookEnableRequest(resource_gid='project'),
                        Organization(id=1), competing_db)
                assert overlap.value.status_code == 409
            raise AsanaTransientError('registration failed')
        def close(self): pass
    monkeypatch.setattr(asana_integration, 'AsanaClient', lambda token: Provider())
    with sessions() as db:
        with pytest.raises(HTTPException) as failure:
            asana_integration.asana_webhook_enable(
                asana_integration.AsanaWebhookEnableRequest(resource_gid='project'), Organization(id=1), db)
        assert failure.value.status_code == 502
        db.expire_all()
        row=db.query(AsanaIntegration).one()
        assert row.webhook_url_token == 'old-url'
        assert row.webhook_gid == 'old-hook'
        assert decrypt_api_key(row.webhook_secret) == 'old-secret'


def test_identical_handshake_retry_is_idempotent_but_different_secret_rejected(sessions):
    with sessions() as db:
        request=Request({'type':'http','headers':[(b'x-hook-secret',b'old-secret')]})
        response=Response()
        asyncio.run(asana_webhook.asana_webhook_inbound('old-url',request,response,db))
        assert response.headers['X-Hook-Secret'] == 'old-secret'
        with pytest.raises(HTTPException) as error:
            request=Request({'type':'http','headers':[(b'x-hook-secret',b'imposter-secret')]})
            asyncio.run(asana_webhook.asana_webhook_inbound('old-url',request,Response(),db))
        assert error.value.status_code == 401


def test_disable_during_registration_cannot_restore_or_resurrect_callback(sessions, monkeypatch):
    class Provider:
        def create_webhook(self, resource_gid, target_url):
            with sessions() as competing_db:
                competing_db.query(AsanaIntegration).update({
                    AsanaIntegration.webhook_url_token:None,
                    AsanaIntegration.webhook_gid:None,
                    AsanaIntegration.webhook_secret:None})
                competing_db.commit()
            return {'gid':'abandoned-hook'}
        def close(self): pass
    monkeypatch.setattr(asana_integration, 'AsanaClient', lambda token: Provider())
    with sessions() as db:
        with pytest.raises(HTTPException) as error:
            asana_integration.asana_webhook_enable(
                asana_integration.AsanaWebhookEnableRequest(resource_gid='project'), Organization(id=1), db)
        assert error.value.status_code == 409
        db.expire_all()
        row=db.query(AsanaIntegration).one()
        assert row.webhook_url_token is None and row.webhook_gid is None and row.webhook_secret is None
