from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_name = Column(String, nullable=False)
    status = Column(String) # firing, resolved
    labels = Column(Text, nullable=True) # Stored as JSON string
    annotations = Column(Text, nullable=True) # Stored as JSON string
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    incident = relationship("Incident", backref="alerts")
