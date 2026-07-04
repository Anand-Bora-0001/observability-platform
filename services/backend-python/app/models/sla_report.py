from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base

class SLAReport(Base):
    __tablename__ = "sla_reports"

    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    
    uptime_percentage = Column(Float, nullable=False) # Monthly
    daily_uptime_percentage = Column(Float, nullable=True)
    weekly_uptime_percentage = Column(Float, nullable=True)
    total_downtime_minutes = Column(Float, default=0.0)
    mttr_minutes = Column(Float, nullable=True) # Mean Time to Recovery
    mtbf_hours = Column(Float, nullable=True) # Mean Time Between Failures
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    server = relationship("Server", backref="sla_reports")
