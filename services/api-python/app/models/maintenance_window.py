from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class MaintenanceWindow(Base):
    __tablename__ = "maintenance_windows"

    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=True) # If null, applies to all
    title = Column(String, index=True)
    description = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    server = relationship("Server")
