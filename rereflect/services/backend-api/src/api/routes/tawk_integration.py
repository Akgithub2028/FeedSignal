"""Admin-controlled tawk.to property registration. No provider password or API key needed."""
import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field, SecretStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.api.dependencies import get_current_org, require_admin_or_owner
from src.database.session import get_db
from src.models import FeedbackSource, Organization, TawkIntegration
from src.utils.encryption import encrypt_api_key

router = APIRouter(prefix="/api/v1/integrations/tawk", tags=["tawk"],
                   dependencies=[Depends(require_admin_or_owner)])


class TawkConnect(BaseModel):
    property_id: str = Field(pattern=r"^[a-f0-9]{24}$")
    webhook_secret: SecretStr
    name: str = Field(default="tawk.to support", min_length=1, max_length=255)


def connection_status(row, source):
    base = (os.getenv("BACKEND_URL") or "").rstrip("/")
    return {"connected": bool(row and source and row.is_active and source.is_active),
            "property_id": row.property_id if row else None,
            "source_id": source.id if source else None,
            "name": source.name if source else None,
            "webhook_url": base + "/api/v1/webhooks/tawk/events" if base else None,
            "last_event_at": source.last_event_at if source else None,
            "events_processed": (source.events_processed or 0) if source else 0}


@router.get("/status")
def get_status(org: Organization = Depends(get_current_org), db: Session = Depends(get_db)):
    row = db.query(TawkIntegration).filter_by(organization_id=org.id).first()
    source = db.get(FeedbackSource, row.source_id) if row else None
    return connection_status(row, source)


@router.post("/connect", status_code=201)
def connect(data: TawkConnect, org: Organization = Depends(get_current_org), db: Session = Depends(get_db)):
    secret = data.webhook_secret.get_secret_value()
    if not 16 <= len(secret) <= 512:
        raise HTTPException(400, "Webhook secret must contain 16–512 characters.")
    try:
        encrypted = encrypt_api_key(secret)
    except (ValueError, TypeError):
        raise HTTPException(503, "Configure the server encryption key before connecting tawk.to.") from None
    # Serializes reconnects for one tenant; property uniqueness also protects cross-tenant races.
    db.query(Organization).filter_by(id=org.id).with_for_update().one()
    row = db.query(TawkIntegration).filter_by(organization_id=org.id).first()
    claimed = db.query(TawkIntegration).filter_by(property_id=data.property_id).first()
    if claimed and claimed.organization_id != org.id:
        raise HTTPException(409, "Property is already registered.")
    source = db.get(FeedbackSource, row.source_id) if row else None
    if source is None:
        source = FeedbackSource(organization_id=org.id, source_type="tawk", auto_import=True)
        db.add(source); db.flush()
        row = TawkIntegration(organization_id=org.id, source_id=source.id)
        db.add(row)
    source.name = data.name
    source.provider_config = {"property_id": data.property_id}
    source.triggers = {"all_messages": True}
    source.auto_import = True
    source.is_active = True
    row.property_id = data.property_id
    row.webhook_secret = encrypted
    row.is_active = True
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(409, "Property is already registered.") from None
    return connection_status(row, source)


@router.delete("/disconnect")
def disconnect(org: Organization = Depends(get_current_org), db: Session = Depends(get_db)):
    db.query(Organization).filter_by(id=org.id).with_for_update().one()
    row = db.query(TawkIntegration).filter_by(organization_id=org.id).with_for_update().first()
    if row:
        source = db.query(FeedbackSource).filter_by(id=row.source_id).with_for_update().first()
        row.is_active = False
        if source: source.is_active = False
        db.commit()
    return {"success": True}
