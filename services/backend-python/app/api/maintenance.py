from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.maintenance_window import MaintenanceWindow
from app.schemas.maintenance_window import MaintenanceWindowCreate, MaintenanceWindowResponse

router = APIRouter()

@router.post("/", response_model=MaintenanceWindowResponse)
def create_maintenance_window(
    *,
    db: Session = Depends(get_db),
    window_in: MaintenanceWindowCreate,
) -> Any:
    window = MaintenanceWindow(**window_in.model_dump())
    db.add(window)
    db.commit()
    db.refresh(window)
    return window

@router.get("/", response_model=List[MaintenanceWindowResponse])
def read_maintenance_windows(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    windows = db.query(MaintenanceWindow).offset(skip).limit(limit).all()
    return windows
