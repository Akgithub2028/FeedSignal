"""Real PostgreSQL locking regression; opt in with an isolated test DB URL."""
import asyncio
import os
import uuid
from datetime import datetime, timedelta

import httpx
import pytest
from cryptography.fernet import Fernet
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.models import Base, Organization, User
from src.models.linear_integration import LinearIntegration
from src.utils.encryption import encrypt_api_key


def test_simultaneous_expired_grants_do_not_block_event_loop(monkeypatch):
    from src.services import linear_tokens
    url = os.environ.get('LINEAR_TEST_POSTGRES_URL')
    if not url:
        pytest.skip('Requires an isolated PostgreSQL test database')
    monkeypatch.setenv('LLM_ENCRYPTION_KEY', Fernet.generate_key().decode())
    monkeypatch.setenv('LINEAR_CLIENT_ID', 'test-client')
    monkeypatch.setenv('LINEAR_CLIENT_SECRET', 'test-secret')
    schema = 'linear_test_' + uuid.uuid4().hex
    base_engine = create_engine(url, connect_args={'options':'-c lock_timeout=500ms'})
    with base_engine.begin() as connection:
        connection.execute(text(f'CREATE SCHEMA {schema}'))
    engine = base_engine.execution_options(schema_translate_map={None:schema})
    factory = sessionmaker(bind=engine)
    try:
        Base.metadata.create_all(engine, tables=[Organization.__table__, User.__table__, LinearIntegration.__table__])
        with factory() as db:
            db.add(Organization(id=1, name='Lock test'))
            db.flush()
            row = LinearIntegration(organization_id=1, linear_org_id='test', linear_org_name='Test',
                access_token=encrypt_api_key('old'), refresh_token=encrypt_api_key('refresh'),
                token_expires_at=datetime.utcnow()-timedelta(seconds=1), webhook_secret=encrypt_api_key('hook'))
            db.add(row)
            db.commit()
            integration_id = row.id

        async def concurrent():
            refreshing = asyncio.Event()
            calls = []
            async def endpoint(request):
                calls.append(request.url.path)
                refreshing.set()
                await asyncio.sleep(0.15)
                return httpx.Response(200, json={'access_token':'renewed', 'refresh_token':'rotated', 'expires_in':86400})
            original_client = httpx.AsyncClient
            monkeypatch.setattr(linear_tokens.httpx, 'AsyncClient', lambda **kwargs: original_client(transport=httpx.MockTransport(endpoint), **kwargs))
            with factory() as first, factory() as second:
                async def competing():
                    await refreshing.wait()
                    return await linear_tokens.get_linear_access_token(second, integration_id)
                results = await asyncio.wait_for(asyncio.gather(
                    linear_tokens.get_linear_access_token(first, integration_id), competing()), timeout=5)
            assert results == ['renewed', 'renewed']
            assert calls == ['/oauth/token']
        asyncio.run(concurrent())
    finally:
        with base_engine.begin() as connection:
            connection.execute(text(f'DROP SCHEMA {schema} CASCADE'))
        base_engine.dispose()
