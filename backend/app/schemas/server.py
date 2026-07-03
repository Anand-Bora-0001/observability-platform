from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServerBase(BaseModel):
    hostname: str
    ip_address: str
    os_type: Optional[str] = None
    status: Optional[str] = "active"

class ServerCreate(ServerBase):
    pass

class ServerUpdate(ServerBase):
    hostname: Optional[str] = None
    ip_address: Optional[str] = None

class ServerResponse(ServerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
