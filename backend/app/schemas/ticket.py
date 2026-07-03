from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "medium"
    status: Optional[str] = "open"
    assignee_id: Optional[int] = None
    incident_id: Optional[int] = None

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    title: Optional[str] = None

class TicketResponse(TicketBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None

    class Config:
        from_attributes = True
