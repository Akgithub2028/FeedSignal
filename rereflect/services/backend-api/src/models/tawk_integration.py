from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from .base import Base


class TawkIntegration(Base):
    """One owner-configured support property per tenant; credentials never in source JSON."""
    __tablename__ = "tawk_integrations"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False, unique=True)
    property_id = Column(String(24), nullable=False, unique=True)
    source_id = Column(Integer, ForeignKey("feedback_sources.id", ondelete="CASCADE"), nullable=False, unique=True)
    webhook_secret = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
