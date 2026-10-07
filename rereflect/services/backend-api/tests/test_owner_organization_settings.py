"""Organization owners retain the same settings permission as admins."""
from types import SimpleNamespace
from unittest.mock import Mock
import pytest
from fastapi import HTTPException
from src.api.routes.organizations import OrganizationUpdateRequest, update_my_organization


@pytest.mark.parametrize('role', ['owner', 'admin'])
def test_owner_and_admin_can_rename_own_organization(role):
    org = SimpleNamespace(id=1, name='Admin Organization', plan='enterprise')
    result = update_my_organization(OrganizationUpdateRequest(name='FeedSignal'),
                                   SimpleNamespace(role=role), org, Mock())
    assert result is org
    assert org.name == 'FeedSignal'
    assert org.plan == 'enterprise'


@pytest.mark.parametrize('role', ['member', 'viewer'])
def test_other_roles_cannot_change_organization(role):
    org = SimpleNamespace(id=1, name='Unchanged', plan='free')
    with pytest.raises(HTTPException) as error:
        update_my_organization(OrganizationUpdateRequest(name='FeedSignal'),
                               SimpleNamespace(role=role), org, Mock())
    assert error.value.status_code == 403
    assert org.name == 'Unchanged'
