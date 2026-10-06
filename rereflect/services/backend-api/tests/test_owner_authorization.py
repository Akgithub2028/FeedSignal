import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.api import dependencies
from src.api.routes import team
from src.models import Organization, User


@pytest.mark.parametrize('path', ['/team/invites', '/team/invite'])
def test_upstream_email_does_not_grant_owner_invite_privilege(path):
    app = FastAPI()
    app.include_router(team.router, prefix='/team')
    app.dependency_overrides[dependencies.get_current_user] = lambda: User(
        id=1, email='support@rereflect.ca', role='owner', is_system_admin=False,
        organization_id=1,
    )
    app.dependency_overrides[dependencies.get_current_org] = lambda: Organization(id=1, name='Test')
    app.dependency_overrides[dependencies.require_admin_or_owner] = lambda: True
    app.dependency_overrides[dependencies.check_seat_limit] = lambda: True
    # Rejection must precede DB access or side effects.
    app.dependency_overrides[team.get_db] = lambda: None
    with TestClient(app) as client:
        response = client.post(path, json={'email': 'new-owner@example.com', 'role': 'owner'})
    assert response.status_code == 403
    assert 'super admin' in response.json()['detail']
