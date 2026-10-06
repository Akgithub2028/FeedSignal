"""Real stored credentials and provider-boundary tests for 2026 Linear OAuth."""
import asyncio
from datetime import datetime, timedelta
from urllib.parse import parse_qs

import httpx
import pytest
from cryptography.fernet import Fernet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base, Organization, User
from src.models.linear_integration import LinearIntegration
from src.models.linear_integration import LinearStatusMapping
from src.utils.encryption import decrypt_api_key, encrypt_api_key


@pytest.fixture
def database(tmp_path, monkeypatch):
    monkeypatch.setenv('LLM_ENCRYPTION_KEY', Fernet.generate_key().decode())
    monkeypatch.setenv('LINEAR_CLIENT_ID', 'owner-test-client')
    monkeypatch.setenv('LINEAR_CLIENT_SECRET', 'owner-test-secret')
    engine = create_engine(f"sqlite:///{tmp_path / 'linear.sqlite'}")
    Base.metadata.create_all(engine, tables=[Organization.__table__, User.__table__, LinearIntegration.__table__, LinearStatusMapping.__table__])
    with sessionmaker(bind=engine)() as db:
        db.add(Organization(id=1, name='Owner'))
        db.commit()
        yield db
    engine.dispose()


def connected(database, expired=False):
    row = LinearIntegration(organization_id=1, access_token=encrypt_api_key('old-access'),
        refresh_token=encrypt_api_key('old-refresh'),
        token_expires_at=datetime.utcnow() + timedelta(seconds=-1 if expired else 3600),
        linear_org_id='owner-linear-org', linear_org_name='FeedSignal',
        webhook_secret=encrypt_api_key('owner-webhook'), is_active=True)
    database.add(row)
    database.commit()
    return row


def test_store_keeps_both_linear_credentials_encrypted(database):
    from src.services.linear_tokens import store_linear_tokens
    row = LinearIntegration(organization_id=1, linear_org_id='owner-linear-org',
        linear_org_name='FeedSignal', webhook_secret=encrypt_api_key('webhook'))
    before = datetime.utcnow()
    store_linear_tokens(row, {'access_token':'owner-access', 'refresh_token':'owner-refresh', 'expires_in':86400})
    database.add(row)
    database.commit()
    database.expire_all()
    stored = database.query(LinearIntegration).one()
    assert stored.access_token != 'owner-access'
    assert stored.refresh_token != 'owner-refresh'
    assert decrypt_api_key(stored.access_token) == 'owner-access'
    assert decrypt_api_key(stored.refresh_token) == 'owner-refresh'
    assert before + timedelta(seconds=86400) <= stored.token_expires_at <= datetime.utcnow() + timedelta(seconds=86400)


@pytest.mark.parametrize('response', [
    {'access_token':'new', 'expires_in':86400},
    {'access_token':'new', 'refresh_token':'next', 'expires_in':0},
    {'access_token':'', 'refresh_token':'next', 'expires_in':86400},
])
def test_invalid_grant_never_overwrites_working_credentials(database, response):
    from src.services.linear_tokens import store_linear_tokens
    row = connected(database)
    previous = (row.access_token, row.refresh_token, row.token_expires_at)
    with pytest.raises(ValueError):
        store_linear_tokens(row, response)
    assert (row.access_token, row.refresh_token, row.token_expires_at) == previous


def provider(monkeypatch, handler):
    from src.services import linear_tokens
    real_client = httpx.AsyncClient
    monkeypatch.setattr(linear_tokens.httpx, 'AsyncClient', lambda **kwargs: real_client(transport=httpx.MockTransport(handler), **kwargs))


def test_valid_access_token_does_not_consume_refresh_token(database, monkeypatch):
    from src.services.linear_tokens import get_linear_access_token
    row = connected(database)
    def unexpected(_request):
        pytest.fail('Unexpired token must not contact the token endpoint')
    provider(monkeypatch, unexpected)
    assert asyncio.run(get_linear_access_token(database, row.id)) == 'old-access'
    assert decrypt_api_key(row.refresh_token) == 'old-refresh'


def test_expired_token_rotates_both_credentials_durably(database, monkeypatch):
    from src.services.linear_tokens import get_linear_access_token
    row = connected(database, expired=True)
    def refresh(request):
        assert str(request.url) == 'https://api.linear.app/oauth/token'
        assert parse_qs(request.content.decode()) == {
            'grant_type':['refresh_token'], 'refresh_token':['old-refresh'],
            'client_id':['owner-test-client'], 'client_secret':['owner-test-secret']}
        return httpx.Response(200, json={'access_token':'new-access', 'refresh_token':'new-refresh', 'expires_in':86400, 'token_type':'Bearer', 'scope':'read write admin'})
    provider(monkeypatch, refresh)
    assert asyncio.run(get_linear_access_token(database, row.id)) == 'new-access'
    database.expire_all()
    stored = database.query(LinearIntegration).one()
    assert decrypt_api_key(stored.access_token) == 'new-access'
    assert decrypt_api_key(stored.refresh_token) == 'new-refresh'
    assert stored.token_expires_at > datetime.utcnow() + timedelta(hours=23)


def test_failed_refresh_preserves_stored_credentials(database, monkeypatch):
    from src.services.linear_tokens import get_linear_access_token, LinearTokenError
    row = connected(database, expired=True)
    previous = (row.access_token, row.refresh_token, row.token_expires_at)
    provider(monkeypatch, lambda request: httpx.Response(401, json={'error':'invalid_grant'}))
    with pytest.raises(LinearTokenError) as failure:
        asyncio.run(get_linear_access_token(database, row.id))
    assert failure.value.status_code == 409
    assert 'Reconnect Linear' in str(failure.value)
    database.expire_all()
    stored = database.query(LinearIntegration).one()
    assert (stored.access_token, stored.refresh_token, stored.token_expires_at) == previous


def test_inactive_connection_cannot_be_used(database):
    from src.services.linear_tokens import get_linear_access_token
    row = connected(database)
    row.is_active = False
    database.commit()
    with pytest.raises(ValueError, match='Reconnect'):
        asyncio.run(get_linear_access_token(database, row.id))


def test_oauth_callback_persists_a_renewable_encrypted_grant(database, monkeypatch):
    from src.api.routes import linear_integration
    from src.services.oauth_state import sign_oauth_state
    monkeypatch.setattr(linear_integration, 'BACKEND_URL', 'http://localhost:8000')
    def handler(request):
        if request.url.path == '/oauth/token':
            return httpx.Response(200, json={'access_token':'owner-callback-access', 'refresh_token':'owner-callback-refresh', 'expires_in':86400, 'token_type':'Bearer', 'scope':'read write admin'})
        return httpx.Response(200, json={'data':{'organization':{'id':'owner-linear-org', 'name':'FeedSignal', 'urlKey':'feedsignal'}}})
    provider(monkeypatch, handler)
    state = sign_oauth_state(1, 'linear', user_id=1)
    result = asyncio.run(linear_integration.linear_oauth_callback(code='test-code', state=state, error=None, db=database))
    assert 'oauth_success=true' in result.headers['location']
    stored = database.query(LinearIntegration).one()
    assert stored.access_token != 'owner-callback-access'
    assert decrypt_api_key(stored.access_token) == 'owner-callback-access'
    assert decrypt_api_key(stored.refresh_token) == 'owner-callback-refresh'


def test_connection_test_sends_decrypted_access_token(database, monkeypatch):
    from src.api.routes import linear_integration
    connected(database)
    def handler(request):
        assert request.headers['Authorization'] == 'Bearer old-access'
        return httpx.Response(200, json={'data':{'organization':{'id':'owner-linear-org', 'name':'FeedSignal', 'urlKey':'feedsignal'}}})
    provider(monkeypatch, handler)
    result = asyncio.run(linear_integration.test_linear_connection(current_org=Organization(id=1), db=database))
    assert result['success'] is True


def test_linear_reply_refreshes_before_sending_a_comment(database, monkeypatch):
    from src.api.routes.feedback_responses import _dispatch_send
    from src.models.feedback import FeedbackItem
    connected(database, expired=True)
    def handler(request):
        if request.url.path == '/oauth/token':
            return httpx.Response(200, json={'access_token':'new-access', 'refresh_token':'new-refresh', 'expires_in':86400, 'token_type':'Bearer', 'scope':'read write admin'})
        assert request.headers['Authorization'] == 'Bearer new-access'
        assert request.read().decode().find('owner-issue') >= 0
        return httpx.Response(200, json={'data':{'commentCreate':{'success':True, 'comment':{'id':'owner-comment'}}}})
    provider(monkeypatch, handler)
    result = asyncio.run(_dispatch_send('linear', 'Owner smoke response',
        FeedbackItem(id=1, organization_id=1, text='Test', source_metadata={'issue_id':'owner-issue'}),
        Organization(id=1), database))
    assert result['success'] is True
    database.expire_all()
    assert decrypt_api_key(database.query(LinearIntegration).one().refresh_token) == 'new-refresh'


def test_linear_reply_reports_revoked_grant_without_exposing_provider_response(database, monkeypatch):
    from src.api.routes.feedback_responses import _dispatch_send
    from src.models.feedback import FeedbackItem
    connected(database, expired=True)
    provider(monkeypatch, lambda request: httpx.Response(401, json={'error':'invalid_grant', 'private':'provider-secret'}))
    result = asyncio.run(_dispatch_send('linear', 'Reply',
        FeedbackItem(id=1, organization_id=1, text='Test', source_metadata={'issue_id':'owner-issue'}),
        Organization(id=1), database))
    assert result == {'success':False, 'error':'Reconnect Linear: the OAuth grant is no longer valid.'}


def test_linear_team_route_returns_reconnect_error_for_legacy_connection(database):
    from fastapi import HTTPException
    from src.api.routes.linear_integration import get_linear_teams
    row = connected(database, expired=True)
    row.refresh_token = None
    database.commit()
    with pytest.raises(HTTPException) as failure:
        asyncio.run(get_linear_teams(current_org=Organization(id=1), db=database))
    assert failure.value.status_code == 409
    assert 'Reconnect Linear' in failure.value.detail
