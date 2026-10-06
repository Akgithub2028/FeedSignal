"""Encrypted, durable token rotation for Linear's 24-hour OAuth grants."""
import asyncio
import os
from datetime import datetime, timedelta

import httpx
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError, SQLAlchemyError

from src.models.linear_integration import LinearIntegration
from src.utils.encryption import decrypt_api_key, encrypt_api_key


class LinearTokenError(ValueError):
    """Safe operator/customer message, without provider response credentials."""
    def __init__(self, message: str, status_code: int = 409):
        super().__init__(message)
        self.status_code = status_code


def store_linear_tokens(integration: LinearIntegration, token_data: dict) -> None:
    access = token_data.get('access_token')
    refresh = token_data.get('refresh_token')
    lifetime = token_data.get('expires_in')
    if not isinstance(access, str) or not access or not isinstance(refresh, str) or not refresh:
        raise ValueError('Linear returned an incomplete OAuth grant; reconnect Linear.')
    if isinstance(lifetime, bool):
        raise ValueError('Linear returned an invalid token expiry.')
    try:
        seconds = int(lifetime)
    except (TypeError, ValueError):
        raise ValueError('Linear returned an invalid token expiry.') from None
    if seconds <= 0:
        raise ValueError('Linear returned an invalid token expiry.')
    # Validate/encrypt everything before changing an existing working grant.
    access_cipher = encrypt_api_key(access)
    refresh_cipher = encrypt_api_key(refresh)
    expires = datetime.utcnow() + timedelta(seconds=seconds)
    integration.access_token = access_cipher
    integration.refresh_token = refresh_cipher
    integration.token_expires_at = expires


async def get_linear_access_token(db: Session, integration_id: int) -> str:
    """Return a usable token; serialize refreshes with a PostgreSQL row lock.

    Call before other route mutations. Both rotating tokens are committed
    together before the caller performs its provider operation. API and
    response routes share this path; no worker clock is needed for refresh.
    """
    query = db.query(LinearIntegration).filter(LinearIntegration.id == integration_id)
    integration = query.first()
    if not integration or not integration.is_active:
        raise LinearTokenError('Reconnect Linear: no active connection.')

    def current(row):
        return row.token_expires_at is not None and row.token_expires_at > datetime.utcnow() + timedelta(seconds=60)

    if current(integration):
        try:
            return decrypt_api_key(integration.access_token)
        except ValueError:
            raise LinearTokenError('Reconnect Linear: stored credentials cannot be read.') from None
    try:
        # A synchronous blocking lock would freeze this event loop while the
        # lock holder awaits HTTP. NOWAIT lets the competing request yield.
        deadline = asyncio.get_running_loop().time() + 35
        while True:
            try:
                integration = query.populate_existing().with_for_update(nowait=True).first()
                break
            except OperationalError as exc:
                db.rollback()
                if getattr(exc.orig, 'pgcode', None) != '55P03':
                    raise
                if asyncio.get_running_loop().time() >= deadline:
                    raise LinearTokenError('Linear token renewal is busy; retry shortly.', 503) from None
                await asyncio.sleep(0.1)
        if not integration or not integration.is_active:
            raise LinearTokenError('Reconnect Linear: no active connection.')
        # Another request may already have refreshed while this one waited.
        if current(integration):
            token = decrypt_api_key(integration.access_token)
            db.commit()  # Release the lock before the caller's provider request.
            return token
        if not integration.refresh_token:
            raise LinearTokenError('Reconnect Linear to obtain a renewable OAuth grant.')
        client_id = os.environ.get('LINEAR_CLIENT_ID')
        client_secret = os.environ.get('LINEAR_CLIENT_SECRET')
        if not client_id or not client_secret:
            raise LinearTokenError('Linear OAuth is not configured; contact support.', 503)
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post('https://api.linear.app/oauth/token', data={
                'grant_type':'refresh_token',
                'refresh_token':decrypt_api_key(integration.refresh_token),
                'client_id':client_id, 'client_secret':client_secret,
            })
            response.raise_for_status()
            store_linear_tokens(integration, response.json())
        db.commit()
        return decrypt_api_key(integration.access_token)
    except LinearTokenError:
        db.rollback()
        raise
    except httpx.HTTPStatusError as exc:
        db.rollback()
        if exc.response.status_code in (400, 401):
            raise LinearTokenError('Reconnect Linear: the OAuth grant is no longer valid.') from None
        raise LinearTokenError('Linear token renewal is temporarily unavailable; retry shortly.', 503) from None
    except httpx.RequestError:
        db.rollback()
        raise LinearTokenError('Linear token renewal is temporarily unavailable; retry shortly.', 503) from None
    except ValueError:
        db.rollback()
        raise LinearTokenError('Reconnect Linear: stored credentials or token response are invalid.') from None
    except SQLAlchemyError:
        db.rollback()
        raise LinearTokenError('Linear credentials are temporarily unavailable; retry shortly.', 503) from None
    except Exception:
        db.rollback()
        raise
