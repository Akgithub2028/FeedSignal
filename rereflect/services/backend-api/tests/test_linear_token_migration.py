"""Run the owner OAuth migration against real legacy database rows."""
import importlib.util
from pathlib import Path

import pytest
import sqlalchemy as sa
from alembic.migration import MigrationContext
from alembic.operations import Operations
from cryptography.fernet import Fernet


def migration():
    path = Path(__file__).parents[1] / 'alembic/versions/fe20261006a1_linear_refresh_tokens.py'
    spec = importlib.util.spec_from_file_location('linear_owner_migration', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def legacy_database():
    engine = sa.create_engine('sqlite://')
    meta = sa.MetaData()
    table = sa.Table('linear_integrations', meta, sa.Column('id', sa.Integer, primary_key=True), sa.Column('access_token', sa.Text, nullable=False))
    meta.create_all(engine)
    return engine, table


def test_upgrade_encrypts_legacy_tokens_without_double_encryption(monkeypatch):
    key = Fernet.generate_key()
    monkeypatch.setenv('LLM_ENCRYPTION_KEY', key.decode())
    encrypted = Fernet(key).encrypt(b'already-encrypted').decode()
    engine, table = legacy_database()
    with engine.begin() as connection:
        connection.execute(table.insert(), [{'id':1, 'access_token':'legacy-token'}, {'id':2, 'access_token':encrypted}])
        module = migration()
        with Operations.context(MigrationContext.configure(connection)):
            module.upgrade()
        columns = {c['name'] for c in sa.inspect(connection).get_columns('linear_integrations')}
        assert {'refresh_token', 'token_expires_at'} <= columns
        rows = connection.execute(sa.text('SELECT access_token,refresh_token,token_expires_at FROM linear_integrations ORDER BY id')).all()
        assert rows[0][0] != 'legacy-token'
        assert Fernet(key).decrypt(rows[0][0].encode()) == b'legacy-token'
        assert rows[1][0] == encrypted
        assert rows[0][1:] == (None, None)
        with Operations.context(MigrationContext.configure(connection)):
            module.downgrade()
        assert {c['name'] for c in sa.inspect(connection).get_columns('linear_integrations')} == {'id', 'access_token'}
        assert Fernet(key).decrypt(connection.execute(sa.text('SELECT access_token FROM linear_integrations WHERE id=1')).scalar().encode()) == b'legacy-token'


def test_missing_key_aborts_before_altering_a_populated_database(monkeypatch):
    monkeypatch.delenv('LLM_ENCRYPTION_KEY', raising=False)
    engine, table = legacy_database()
    with engine.begin() as connection:
        connection.execute(table.insert(), {'id':1, 'access_token':'legacy-token'})
        with Operations.context(MigrationContext.configure(connection)):
            with pytest.raises(RuntimeError, match='LLM_ENCRYPTION_KEY'):
                migration().upgrade()
        assert {c['name'] for c in sa.inspect(connection).get_columns('linear_integrations')} == {'id', 'access_token'}
        assert connection.execute(sa.text('SELECT access_token FROM linear_integrations')).scalar() == 'legacy-token'
