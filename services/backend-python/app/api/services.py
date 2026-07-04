from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceResponse, ServiceUpdate

router = APIRouter()

@router.post("/", response_model=ServiceResponse)
def create_service(
    *,
    db: Session = Depends(get_db),
    service_in: ServiceCreate,
) -> Any:
    service = Service(**service_in.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

@router.get("/", response_model=List[ServiceResponse])
def read_services(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    services = db.query(Service).offset(skip).limit(limit).all()
    return services

@router.get("/{service_id}", response_model=ServiceResponse)
def read_service(
    *,
    db: Session = Depends(get_db),
    service_id: int,
) -> Any:
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service
