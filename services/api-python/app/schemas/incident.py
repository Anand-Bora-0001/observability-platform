from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class IncidentBase(BaseModel):
    title: str
    description: Optional[str] = None
    severity: Optional[str] = "warning"
    status: Optional[str] = "open"

class IncidentCreate(IncidentBase):
    pass

class IncidentResponse(IncidentBase):
    id: int
    created_at: datetime
    resolved_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Schemas for Alertmanager webhook payload
class AlertmanagerAlert(BaseModel):
    status: str
    labels: Dict[str, str]
    annotations: Dict[str, str]
    startsAt: str
    endsAt: str
    generatorURL: str
    fingerprint: str

class AlertmanagerPayload(BaseModel):
    receiver: str
    status: str
    alerts: List[AlertmanagerAlert]
    groupLabels: Dict[str, str]
    commonLabels: Dict[str, str]
    commonAnnotations: Dict[str, str]
    externalURL: str
    version: str
    groupKey: str
