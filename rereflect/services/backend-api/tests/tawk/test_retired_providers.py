"""Retired providers cannot reconnect or capture; history remains readable."""
import pytest
from src.models import Organization, Integration, FeedbackSource
RETIRED = ("salesforce", "intercom", "zendesk")

@pytest.mark.parametrize("provider", RETIRED)
def test_source_not_offered_or_created(client, auth_headers, provider):
    assert provider not in {i["type"] for i in client.get("/api/v1/feedback-sources/types").json()}
    assert client.post("/api/v1/feedback-sources/", headers=auth_headers,
        json={"source_type":provider,"name":"Retired source"}).status_code == 400

@pytest.mark.parametrize("provider", RETIRED)
def test_existing_source_cannot_be_enabled(client, db, auth_headers, provider):
    row=FeedbackSource(organization_id=db.query(Organization).one().id,source_type=provider,name="Historical",is_active=False)
    db.add(row);db.commit()
    assert client.patch(f"/api/v1/feedback-sources/{row.id}",headers=auth_headers,json={"is_active":True}).status_code==410
    db.refresh(row);assert row.is_active is False
    assert client.get(f"/api/v1/feedback-sources/{row.id}",headers=auth_headers).status_code==200

@pytest.mark.parametrize("provider", RETIRED)
def test_generic_integration_cannot_be_enabled(client,db,auth_headers,provider):
    from src.api.routes.integrations import router
    client.app.include_router(router)
    row=Integration(organization_id=db.query(Organization).one().id,type=provider,name="Historical",config={},is_active=False)
    db.add(row);db.commit()
    assert client.patch(f"/api/v1/integrations/{row.id}",headers=auth_headers,json={"is_active":True}).status_code==410
    assert client.get("/api/v1/integrations/",headers=auth_headers).json()["integrations"]==[]

@pytest.mark.parametrize("path",["/api/v1/integrations/intercom/oauth/connect","/api/v1/integrations/intercom/oauth/callback"])
def test_intercom_oauth_removed(client,auth_headers,path):
    from src.api.routes.integrations import router
    client.app.include_router(router)
    assert client.get(path,headers=auth_headers,follow_redirects=False).status_code==404

@pytest.mark.parametrize("provider",["intercom","zendesk"])
def test_webhook_removed(client,provider):
    from src.api.routes.source_webhooks import router
    client.app.include_router(router)
    assert client.post(f"/api/v1/webhooks/{provider}/events",json={}).status_code==404

def test_response_channel_rejected():
    from pydantic import ValidationError
    from src.api.routes.feedback_responses import SendResponseRequest
    with pytest.raises(ValidationError):
        SendResponseRequest(response_text="Owner test",channel="intercom",source="manual")


def test_historical_salesforce_does_not_block_hubspot(db, auth_headers):
    from datetime import datetime, timezone
    from src.models.salesforce_integration import SalesforceIntegration
    from src.services.crm_integration_common import another_crm_active
    org_id = db.query(Organization).one().id
    db.add(SalesforceIntegration(organization_id=org_id, refresh_token="test-encrypted", connected_at=datetime.now(timezone.utc), is_active=True))
    db.commit()
    assert another_crm_active(db, org_id, exclude_provider="hubspot") is None
