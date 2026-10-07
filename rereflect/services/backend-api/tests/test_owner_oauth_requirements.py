"""Authorization grants must cover the baseline ingestion and webhook paths."""
from urllib.parse import parse_qs, urlparse

from src.api.routes import integrations, linear_integration
from src.models import Organization, User


def test_slack_grant_covers_public_and_private_channel_ingestion(monkeypatch):
    monkeypatch.setattr(integrations, 'SLACK_CLIENT_ID', 'test-client-id')
    monkeypatch.setattr(integrations, 'SLACK_REDIRECT_URI', 'https://api.example.com/slack/callback')
    result = integrations.slack_oauth_connect(name='Owner Slack', current_org=Organization(id=1))
    params = parse_qs(urlparse(result.auth_url).query)
    assert set(params['scope'][0].split(',')) == {
        'chat:write', 'channels:read', 'groups:read', 'channels:history', 'groups:history', 'incoming-webhook'
    }
    assert params['redirect_uri'] == ['https://api.example.com/slack/callback']
    assert params['state'] == [result.state]


def test_linear_grant_covers_automatic_workspace_webhook_creation(monkeypatch):
    monkeypatch.setattr(linear_integration, 'LINEAR_CLIENT_ID', 'test-client-id')
    result = linear_integration.linear_oauth_connect(
        current_org=Organization(id=1), current_user=User(id=1))
    params = parse_qs(urlparse(result.auth_url).query)
    assert set(params['scope'][0].split(',')) == {'read', 'write', 'admin'}
    assert params['state'] == [result.state]
