from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MaintenanceWindowBase(BaseModel):
    server_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    is_active: bool = True

class MaintenanceWindowCreate(MaintenanceWindowBase):
    pass

class MaintenanceWindowResponse(MaintenanceWindowBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
