from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SLAReportBase(BaseModel):
    server_id: int
    month: int
    year: int
    uptime_percentage: float
    daily_uptime_percentage: Optional[float] = None
    weekly_uptime_percentage: Optional[float] = None
    total_downtime_minutes: float = 0.0
    mttr_minutes: Optional[float] = None
    mtbf_hours: Optional[float] = None

class SLAReportCreate(SLAReportBase):
    pass

class SLAReportResponse(SLAReportBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
