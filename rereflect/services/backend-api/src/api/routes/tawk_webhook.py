"""Raw-body HMAC-SHA1 authentication, atomic durable receipts and feedback ingestion."""
import hashlib
import hmac
import json
import logging
from datetime import datetime, timezone
from cryptography.fernet import InvalidToken
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from src.database.session import get_db
from src.models import FeedbackItem, FeedbackSource, FeedbackSourceEvent, TawkIntegration
from src.services.tawk_ingestion import normalize
from src.utils.encryption import decrypt_api_key

router = APIRouter(prefix="/api/v1/webhooks/tawk", tags=["tawk-webhooks"])
logger = logging.getLogger(__name__)
MAX_BODY = 1024 * 1024


def _queue_analysis(feedback_id):
    # Broker I/O is bounded; durable unanalyzed items are recovered by existing Beat.
    from src.background.celery_client import get_celery_app
    app = get_celery_app()
    with app.connection_for_write(connect_timeout=2) as connection:
        connection.transport_options.update(socket_connect_timeout=2, socket_timeout=2, retry_on_timeout=False)
        app.send_task("src.tasks.analysis.analyze_single_feedback", args=[feedback_id],
                      connection=connection, retry=False, ignore_result=True)


@router.post("/events")
async def receive(request: Request, db: Session = Depends(get_db)):
    body = bytearray()
    async for chunk in request.stream():
        if len(body) + len(chunk) > MAX_BODY: raise HTTPException(413, "Payload too large")
        body.extend(chunk)
    try:
        payload = json.loads(body)
        if not isinstance(payload, dict) or not isinstance(payload.get("property"), dict): raise ValueError()
        property_id = payload["property"].get("id")
        if not isinstance(property_id, str) or len(property_id) != 24: raise ValueError()
        event = payload.get("event")
        if not isinstance(event, str) or len(event) > 50: raise ValueError()
    except (ValueError, UnicodeDecodeError, RecursionError):
        raise HTTPException(400, "Invalid webhook payload") from None
    row = db.query(TawkIntegration).filter_by(property_id=property_id, is_active=True).with_for_update().first()
    source = db.query(FeedbackSource).filter_by(id=row.source_id, organization_id=row.organization_id,
                                               source_type="tawk", is_active=True).with_for_update().first() if row else None
    try:
        secret = decrypt_api_key(row.webhook_secret) if row and source else None
    except (ValueError, TypeError, InvalidToken):
        secret = None
    signature = request.headers.get("X-Tawk-Signature", "")
    expected = hmac.new(secret.encode(), body, hashlib.sha1).hexdigest() if secret else ""
    if not expected or len(signature) != 40 or not hmac.compare_digest(expected.encode(), signature.encode()):
        raise HTTPException(401, "Webhook authentication failed")
    event_id = request.headers.get("X-Hook-Event-Id", "")
    if not event_id.strip() or len(event_id) > 255: raise HTTPException(400, "Missing or invalid event ID")
    existing = db.query(FeedbackSourceEvent).filter_by(source_id=source.id, external_event_id=event_id).first()
    if existing: return {"status": "duplicate"}
    try:
        content = normalize(payload)
    except (ValueError, TypeError, KeyError):
        raise HTTPException(400, "Invalid event content") from None
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    receipt = FeedbackSourceEvent(source_id=source.id, organization_id=source.organization_id,
                                  external_event_id=event_id, event_type=event, processed_at=now,
                                  status="ignored", event_data=content)
    db.add(receipt)
    outcome = "ignored"
    feedback_id = None
    if content:
        receipt.external_message_id = content["external_id"]
        previous = db.query(FeedbackSourceEvent).filter(
            FeedbackSourceEvent.source_id == source.id,
            FeedbackSourceEvent.external_message_id == content["external_id"],
            FeedbackSourceEvent.feedback_id.isnot(None),
        ).first()
        if previous:
            receipt.feedback_id = previous.feedback_id
            receipt.status = "ignored"
            outcome = "duplicate"
        else:
            item = FeedbackItem(organization_id=source.organization_id, source="tawk", source_id=source.id,
                                text=content["text"], source_external_id=content["external_id"],
                                customer_email=content["customer_email"], source_metadata=content["metadata"])
            db.add(item); db.flush()
            feedback_id = item.id
            receipt.feedback_id = item.id
            receipt.status = "processed"
            source.events_processed = (source.events_processed or 0) + 1
            outcome = "accepted"
    source.last_event_at = now
    db.commit()  # A successful response always follows durable receipt/feedback acceptance.
    if feedback_id is not None:
        try:
            _queue_analysis(feedback_id)
        except Exception:
            logger.warning("tawk feedback %s awaits periodic analysis recovery", feedback_id)
    return {"status": outcome}
