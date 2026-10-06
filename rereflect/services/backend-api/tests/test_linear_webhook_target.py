"""Exercise webhook creation at the actual provider HTTP boundary."""
import asyncio
import json

import httpx
import pytest

from src.services import linear_client


@pytest.mark.parametrize('team_id', [None, 'owner-team'])
def test_webhook_registration_always_specifies_a_team_target(monkeypatch, team_id):
    original_client = httpx.AsyncClient
    def endpoint(request):
        payload = json.loads(request.content)['variables']['input']
        assert request.headers['Authorization'] == 'Bearer test-token'
        if not payload.get('teamId') and not payload.get('allPublicTeams'):
            return httpx.Response(200, json={'errors':[{'message':'No team id or value for allPublicTeams provided.'}]})
        assert (payload.get('teamId') == team_id) if team_id else payload['allPublicTeams'] is True
        if team_id:
            assert 'allPublicTeams' not in payload
        return httpx.Response(200, json={'data':{'webhookCreate':{'success':True,'webhook':{'id':'owner-hook','url':payload['url'],'enabled':True}}}})
    monkeypatch.setattr(linear_client.httpx, 'AsyncClient', lambda **kwargs: original_client(transport=httpx.MockTransport(endpoint), **kwargs))
    result = asyncio.run(linear_client.LinearClient('test-token').create_webhook('https://api.example.com/inbound', team_id, 'test-signing-secret'))
    assert result['id'] == 'owner-hook'
