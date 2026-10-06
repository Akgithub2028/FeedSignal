import pytest
from fastapi import HTTPException

from src.api.routes.feedback_sources import FeedbackSourceCreate, create_feedback_source
from src.models import Organization


def test_email_source_requires_operator_receiving_domain(monkeypatch):
    monkeypatch.delenv('INBOUND_EMAIL_DOMAIN', raising=False)
    with pytest.raises(HTTPException) as error:
        create_feedback_source(FeedbackSourceCreate(source_type='email', name='Owner inbox'),
                               current_org=Organization(id=1, name='Owner', plan='enterprise'), db=None)
    assert error.value.status_code == 503
    assert 'INBOUND_EMAIL_DOMAIN' in error.value.detail
