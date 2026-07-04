from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.sla_report import SLAReport
from app.schemas.sla_report import SLAReportCreate, SLAReportResponse

router = APIRouter()

@router.post("/", response_model=SLAReportResponse)
def create_sla_report(
    *,
    db: Session = Depends(get_db),
    report_in: SLAReportCreate,
) -> Any:
    report = SLAReport(**report_in.model_dump())
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

@router.get("/", response_model=List[SLAReportResponse])
def read_sla_reports(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    reports = db.query(SLAReport).offset(skip).limit(limit).all()
    return reports
