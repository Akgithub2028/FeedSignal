"""Real owner-scoped Slack reconnect and response-send regressions."""
import asyncio

import httpx
import pytest
from cryptography.fernet import Fernet
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base, Organization
from src.models.integration import Integration
from src.models.feedback_source import FeedbackSource
from src.utils.encryption import encrypt_api_key, decrypt_api_key


@pytest.fixture
def database(tmp_path, monkeypatch):
    monkeypatch.setenv('LLM_ENCRYPTION_KEY', Fernet.generate_key().decode())
    engine = create_engine(f"sqlite:///{tmp_path / 'slack.sqlite'}")
    Base.metadata.create_all(engine, tables=[Organization.__table__, Integration.__table__, FeedbackSource.__table__])
    with sessionmaker(bind=engine)() as db:
        db.add_all([Organization(id=1, name='Owner'), Organization(id=2, name='Other tenant')])
        db.commit()
        yield db
    engine.dispose()


def test_reauthorization_updates_only_the_matching_owner_connection(database, monkeypatch):
    from src.api.routes import integrations
    from src.services.oauth_state import sign_oauth_state
    monkeypatch.setattr(integrations, 'SLACK_CLIENT_ID', 'test-client')
    monkeypatch.setattr(integrations, 'SLACK_CLIENT_SECRET', 'test-secret')
    rows = [Integration(organization_id=org_id, type='slack', name=name,
        config={'integration_type':'oauth', 'team_id':'TOWNER'},
        oauth_access_token=encrypt_api_key('previous'))
        for org_id, name in [(1,'Owner workspace'), (1,'Other destination'), (2,'Owner workspace')]]
    database.add_all(rows)
    database.commit()
    previous_ids = [row.id for row in rows]
    real_client = httpx.Client
    def exchange(request):
        assert request.url.path == '/api/oauth.v2.access'
        return httpx.Response(200, json={'ok':True, 'access_token':'replacement-token',
            'team':{'id':'TOWNER','name':'FeedSignal'}, 'bot_user_id':'UBOT',
            'incoming_webhook':{'channel_id':'CTEST','channel':'feedsignal-test'}})
    monkeypatch.setattr(integrations.httpx, 'Client', lambda **kwargs: real_client(transport=httpx.MockTransport(exchange), **kwargs))
    result = integrations.slack_oauth_callback('test-code', sign_oauth_state(1,'Owner workspace'), error=None, db=database)
    assert result.status_code == 307
    database.expire_all()
    assert database.query(Integration).count() == 3
    owner = database.get(Integration, previous_ids[0])
    assert owner.config['channel_id'] == 'CTEST'
    assert owner.oauth_access_token != 'replacement-token'
    assert decrypt_api_key(owner.oauth_access_token) == 'replacement-token'
    assert all(decrypt_api_key(database.get(Integration, row_id).oauth_access_token) == 'previous' for row_id in previous_ids[1:])


def test_slack_reply_uses_the_stored_encrypted_oauth_token(database, monkeypatch):
    from src.api.routes.feedback_responses import _dispatch_send
    from src.models.feedback import FeedbackItem
    from src.services import response_sender
    database.add(Integration(organization_id=1, type='slack', name='Owner workspace',
        config={'team_id':'TOWNER'}, oauth_access_token=encrypt_api_key('owner-token')))
    database.commit()
    original_client = httpx.AsyncClient
    def send(request):
        assert request.headers['Authorization'] == 'Bearer owner-token'
        assert request.url.path == '/api/chat.postMessage'
        assert b'CTEST' in request.content
        return httpx.Response(200, json={'ok':True})
    monkeypatch.setattr(response_sender.httpx, 'AsyncClient', lambda **kwargs: original_client(transport=httpx.MockTransport(send), **kwargs))
    result = asyncio.run(_dispatch_send('slack','Test reply',
        FeedbackItem(id=1,organization_id=1,text='Test',source_metadata={'channel_id':'CTEST'}),
        Organization(id=1),database))
    assert result == {'success':True,'error':None}


def test_slack_reply_uses_its_linked_source_workspace(database, monkeypatch):
    from src.api.routes.feedback_responses import _dispatch_send
    from src.models.feedback import FeedbackItem
    from src.services import response_sender
    wrong = Integration(organization_id=1,type='slack',name='Other workspace',oauth_access_token=encrypt_api_key('wrong-token'))
    right = Integration(organization_id=1,type='slack',name='Linked workspace',oauth_access_token=encrypt_api_key('linked-token'))
    database.add_all([wrong,right]);database.flush()
    source = FeedbackSource(organization_id=1,integration_id=right.id,source_type='slack',name='Linked source')
    database.add(source);database.commit()
    original_client = httpx.AsyncClient
    def send(request):
        assert request.headers['Authorization'] == 'Bearer linked-token'
        return httpx.Response(200,json={'ok':True})
    monkeypatch.setattr(response_sender.httpx,'AsyncClient',lambda **kwargs:original_client(transport=httpx.MockTransport(send),**kwargs))
    result = asyncio.run(_dispatch_send('slack','Test reply',
        FeedbackItem(id=1,organization_id=1,source_id=source.id,text='Test',source_metadata={'channel_id':'CTEST'}),
        Organization(id=1),database))
    assert result['success'] is True
