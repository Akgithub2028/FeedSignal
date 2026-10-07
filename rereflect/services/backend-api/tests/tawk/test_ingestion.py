"""Owner configuration and real database tests for signed tawk.to ingestion."""
import hashlib
import hmac
import json
from unittest.mock import MagicMock

import pytest
from cryptography.fernet import Fernet

from src.models import FeedbackItem, FeedbackSource, FeedbackSourceEvent, Organization
from src.api.auth import create_access_token

PROPERTY = "a" * 24
SECRET = "owner-test-signing-secret-12345"
CONNECT = "/api/v1/integrations/tawk/connect"
HOOK = "/api/v1/webhooks/tawk/events"


@pytest.fixture(autouse=True)
def configuration(monkeypatch):
    monkeypatch.setenv("LLM_ENCRYPTION_KEY", Fernet.generate_key().decode())
    monkeypatch.setenv("BACKEND_URL", "https://api.example.com")
    app = MagicMock()
    monkeypatch.setattr("src.background.celery_client.get_celery_app", lambda: app)
    return app


def connect(client, headers, property_id=PROPERTY):
    response = client.post(CONNECT, headers=headers, json={
        "property_id": property_id, "webhook_secret": SECRET, "name": "FeedSignal support",
    })
    assert response.status_code == 201, response.text
    return response.json()


def transcript():
    return {"event": "chat:transcript_created", "property": {"id": PROPERTY},
            "time": "2026-10-07T09:00:00Z", "domain": "example.com",
            "chat": {"id": "chat-1", "visitor": {"name": "Anonymous"}, "messages": [
                {"sender": {"t": "s"}, "type": "msg", "msg": "System greeting"},
                {"sender": {"t": "v"}, "type": "msg", "msg": "CSV export crashes."},
                {"sender": {"t": "a"}, "type": "msg", "msg": "Internal agent response"},
                {"sender": {"t": "v"}, "type": "msg", "msg": "Please fix it."},
            ]}}


def deliver(client, payload, event_id="event-1", secret=SECRET, raw=None):
    body = raw if raw is not None else json.dumps(payload).encode()
    return client.post(HOOK, content=body, headers={
        "Content-Type": "application/json", "X-Hook-Event-Id": event_id,
        "X-Tawk-Signature": hmac.new(secret.encode(), body, hashlib.sha1).hexdigest(),
    })


def test_configuration_encrypted_and_never_returned(client, db, auth_headers):
    from src.utils.encryption import decrypt_api_key
    result = connect(client, auth_headers)
    assert result["connected"] is True
    assert result["webhook_url"] == "https://api.example.com" + HOOK
    assert SECRET not in json.dumps(result)
    from src.models.tawk_integration import TawkIntegration
    row = db.query(TawkIntegration).one()
    assert row.webhook_secret != SECRET
    assert decrypt_api_key(row.webhook_secret) == SECRET
    status = client.get("/api/v1/integrations/tawk/status", headers=auth_headers)
    assert status.status_code == 200
    assert "webhook_secret" not in status.text
    source = client.get(f"/api/v1/feedback-sources/{row.source_id}", headers=auth_headers)
    assert SECRET not in source.text


def test_member_cannot_configure(client, member_headers):
    assert client.post(CONNECT, headers=member_headers, json={
        "property_id": PROPERTY, "webhook_secret": SECRET}).status_code == 403


def test_property_cannot_be_claimed_by_another_tenant(client, db, auth_headers):
    connect(client, auth_headers)
    org = Organization(name="Other tenant", plan="pro")
    db.add(org); db.commit()
    from src.models.user import User
    from src.api.auth import hash_password
    user = User(email="second-owner@example.com", password_hash=hash_password("testpassword"),
                organization_id=org.id, role="owner")
    db.add(user); db.commit()
    headers = {"Authorization": "Bearer " + create_access_token({
        "user_id": user.id, "organization_id": org.id, "role": "owner"})}
    response = client.post(CONNECT, headers=headers, json={
        "property_id": PROPERTY, "webhook_secret": SECRET})
    assert response.status_code == 409
    assert db.query(FeedbackSource).count() == 1


def test_reconnect_preserves_source_and_receipts(client, db, auth_headers):
    first = connect(client, auth_headers)
    assert deliver(client, transcript()).status_code == 200
    second = connect(client, auth_headers)
    assert first["source_id"] == second["source_id"]
    assert db.query(FeedbackSource).count() == 1
    assert db.query(FeedbackSourceEvent).count() == 1


@pytest.mark.parametrize("signature", [None, "bad", "f" * 40])
def test_signature_rejects_without_writing(client, db, auth_headers, signature):
    connect(client, auth_headers)
    headers = {"X-Hook-Event-Id": "event-1"}
    if signature is not None: headers["X-Tawk-Signature"] = signature
    response = client.post(HOOK, json=transcript(), headers=headers)
    assert response.status_code == 401
    assert db.query(FeedbackSourceEvent).count() == 0
    assert db.query(FeedbackItem).count() == 0


def test_signature_uses_exact_raw_bytes(client, auth_headers):
    connect(client, auth_headers)
    assert deliver(client, transcript(), raw=json.dumps(transcript(), indent=2).encode()).status_code == 200


def test_missing_event_id_rejected(client, db, auth_headers):
    connect(client, auth_headers)
    assert deliver(client, transcript(), event_id="").status_code == 400
    assert db.query(FeedbackItem).count() == 0


def test_agent_ticket_is_not_customer_feedback(client, db, auth_headers):
    connect(client, auth_headers)
    data = {"event": "ticket:create", "property": {"id": PROPERTY},
            "requester": {"type": "agent"}, "ticket": {"id": "internal", "message": "Agent note"}}
    assert deliver(client, data).json()["status"] == "ignored"
    assert db.query(FeedbackItem).count() == 0


def test_reordered_independent_chats_are_retained(client, db, auth_headers):
    connect(client, auth_headers)
    newer = transcript()
    older = transcript(); older["time"] = "2026-10-07T08:00:00Z"; older["chat"]["id"] = "chat-older"
    assert deliver(client, newer).status_code == 200
    assert deliver(client, older, event_id="older-event").status_code == 200
    assert db.query(FeedbackItem).count() == 2


def test_transcript_only_visitor_text_and_anonymous_contact(client, db, auth_headers, configuration):
    result = connect(client, auth_headers)
    response = deliver(client, transcript())
    assert response.status_code == 200
    item = db.query(FeedbackItem).one()
    assert item.text == "CSV export crashes.\nPlease fix it."
    assert item.source == "tawk" and item.source_id == result["source_id"]
    assert item.customer_email is None
    assert item.source_metadata["property_id"] == PROPERTY
    event = db.query(FeedbackSourceEvent).one()
    assert event.feedback_id == item.id and event.status == "processed"
    assert "Internal agent response" not in json.dumps(event.event_data)
    configuration.send_task.assert_called_once()


def test_duplicate_and_changed_hook_id_do_not_duplicate_feedback(client, db, auth_headers, configuration):
    connect(client, auth_headers)
    assert deliver(client, transcript()).status_code == 200
    assert deliver(client, transcript()).json()["status"] == "duplicate"
    assert deliver(client, transcript(), event_id="event-2").json()["status"] == "duplicate"
    assert db.query(FeedbackItem).count() == 1
    assert db.query(FeedbackSourceEvent).count() == 2
    configuration.send_task.assert_called_once()


def test_unknown_property_and_tampering_rejected(client, db, auth_headers):
    connect(client, auth_headers)
    data = transcript(); data["property"]["id"] = "b" * 24
    assert deliver(client, data).status_code == 401
    assert db.query(FeedbackItem).count() == 0


def test_ticket_and_contact(client, db, auth_headers):
    connect(client, auth_headers)
    data = {"event": "ticket:create", "property": {"id": PROPERTY},
            "requester": {"name": "Test visitor", "email": "visitor@example.com", "type": "visitor"},
            "ticket": {"id": "ticket-1", "humanId": 1, "subject": "Export broken",
                       "message": "<p>Cannot export <b>CSV</b>.</p>"}}
    assert deliver(client, data).status_code == 200
    item = db.query(FeedbackItem).one()
    assert item.text == "Export broken\nCannot export CSV."
    assert item.customer_email == "visitor@example.com"


def test_agent_only_or_unsupported_events_ignored(client, db, auth_headers):
    connect(client, auth_headers)
    data = transcript(); data["chat"]["messages"] = [data["chat"]["messages"][2]]
    assert deliver(client, data).json()["status"] == "ignored"
    data["event"] = "chat:start"
    assert deliver(client, data, event_id="event-2").json()["status"] == "ignored"
    assert db.query(FeedbackItem).count() == 0


@pytest.mark.parametrize("data", [[], {}, {"event": "chat:transcript_created", "property": {"id": PROPERTY}, "chat": []}])
def test_malformed_payloads(client, auth_headers, data):
    connect(client, auth_headers)
    assert deliver(client, data).status_code == 400


def test_large_payload_rejected(client, auth_headers):
    connect(client, auth_headers)
    assert deliver(client, {}, raw=b"x" * (1024 * 1024 + 1)).status_code == 413


def test_broker_failure_preserves_durable_unanalyzed_feedback(client, db, auth_headers, configuration):
    connect(client, auth_headers)
    configuration.send_task.side_effect = ConnectionError("broker unavailable")
    assert deliver(client, transcript()).status_code == 200
    item = db.query(FeedbackItem).one()
    assert item.sentiment_label is None
    assert db.query(FeedbackSourceEvent).one().feedback_id == item.id
    assert deliver(client, transcript()).json()["status"] == "duplicate"
    assert db.query(FeedbackItem).count() == 1


def test_disconnect_blocks_ingestion_preserves_history(client, db, auth_headers):
    connect(client, auth_headers)
    assert deliver(client, transcript()).status_code == 200
    assert client.delete("/api/v1/integrations/tawk/disconnect", headers=auth_headers).status_code == 200
    assert deliver(client, transcript(), event_id="later").status_code == 401
    assert db.query(FeedbackItem).count() == 1


def test_missing_encryption_key_fails_closed(client, db, auth_headers, monkeypatch):
    monkeypatch.delenv("LLM_ENCRYPTION_KEY")
    assert client.post(CONNECT, headers=auth_headers, json={
        "property_id": PROPERTY, "webhook_secret": SECRET}).status_code == 503
    assert db.query(FeedbackSource).count() == 0


def test_generic_source_update_cannot_replace_tawk_routing(client, auth_headers):
    result = connect(client, auth_headers)
    path = f"/api/v1/feedback-sources/{result['source_id']}"
    assert client.patch(path, headers=auth_headers, json={"provider_config": {"property_id": "b" * 24}}).status_code == 400
    assert client.patch(path, headers=auth_headers, json={"auto_import": False}).status_code == 400
    assert client.patch(path, headers=auth_headers, json={"triggers": {"keywords": ["bug"]}}).status_code == 400


def test_publish_happens_after_database_commit(client, db, auth_headers, configuration):
    connect(client, auth_headers)
    observed = []
    def published(*args, **kwargs):
        observed.append((db.in_transaction(), kwargs["retry"]))
    configuration.send_task.side_effect = published
    assert deliver(client, transcript()).status_code == 200
    configuration.send_task.assert_called_once()
    assert observed == [(False, False)]


def test_unconfigured_status_returns_callback_and_no_credentials(client, auth_headers):
    response = client.get("/api/v1/integrations/tawk/status", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["connected"] is False
    assert response.json()["webhook_url"].endswith(HOOK)


def test_postgres_concurrent_deliveries_create_one_feedback(client, db, auth_headers, postgres_engine, monkeypatch):
    if postgres_engine is None: pytest.skip("Needs isolated PostgreSQL schema")
    import asyncio
    from concurrent.futures import ThreadPoolExecutor
    from sqlalchemy.orm import Session
    from starlette.requests import Request
    from src.api.routes import tawk_webhook
    connect(client, auth_headers)
    monkeypatch.setattr(tawk_webhook, "_queue_analysis", lambda _: None)
    body = json.dumps(transcript()).encode()
    signature = hmac.new(SECRET.encode(), body, hashlib.sha1).hexdigest()
    def one(event_id):
        async def receive_body():
            return {"type": "http.request", "body": body, "more_body": False}
        request = Request({"type": "http", "method": "POST", "path": HOOK,
                           "headers": [(b"x-tawk-signature", signature.encode()),
                                       (b"x-hook-event-id", event_id.encode())]}, receive_body)
        with Session(postgres_engine) as session:
            return asyncio.run(tawk_webhook.receive(request, session))["status"]
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(one, ("event-1", "event-2")))
    assert sorted(results) == ["accepted", "duplicate"]
    db.expire_all()
    assert db.query(FeedbackItem).count() == 1
    assert db.query(FeedbackSourceEvent).count() == 2
