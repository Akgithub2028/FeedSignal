"""Encrypt Linear credentials and retain renewable 24-hour OAuth grants.

Revision ID: fe20261006a1
Revises: ad76527a185e
"""
import os

from alembic import op
from cryptography.fernet import Fernet
import sqlalchemy as sa

revision = 'fe20261006a1'
down_revision = 'ad76527a185e'
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()
    rows = connection.execute(sa.text('SELECT id, access_token FROM linear_integrations')).all()
    updates = []
    if rows:
        key = os.environ.get('LLM_ENCRYPTION_KEY')
        if not key:
            raise RuntimeError('LLM_ENCRYPTION_KEY is required before migrating Linear credentials.')
        cipher = Fernet(key.encode())
        # Complete validation before DDL or credential mutations.
        for row_id, token in rows:
            if token.startswith('gAAAAA'):
                cipher.decrypt(token.encode())
            else:
                updates.append({'id':row_id, 'token':cipher.encrypt(token.encode()).decode()})
    op.add_column('linear_integrations', sa.Column('refresh_token', sa.Text(), nullable=True))
    op.add_column('linear_integrations', sa.Column('token_expires_at', sa.DateTime(), nullable=True))
    for update in updates:
        connection.execute(sa.text('UPDATE linear_integrations SET access_token=:token WHERE id=:id'), update)


def downgrade():
    # Do not turn encrypted credentials back into plaintext on rollback.
    # Legacy connections must reauthorize to obtain refresh tokens.
    op.drop_column('linear_integrations', 'token_expires_at')
    op.drop_column('linear_integrations', 'refresh_token')
