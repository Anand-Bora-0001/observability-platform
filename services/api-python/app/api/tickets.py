from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketResponse, TicketUpdate
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=TicketResponse)
def create_ticket(
    *,
    db: Session = Depends(get_db),
    ticket_in: TicketCreate,
) -> Any:
    ticket = Ticket(**ticket_in.model_dump())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

@router.get("/", response_model=List[TicketResponse])
def read_tickets(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    tickets = db.query(Ticket).offset(skip).limit(limit).all()
    return tickets

@router.put("/{ticket_id}/resolve", response_model=TicketResponse)
def resolve_ticket(
    *,
    db: Session = Depends(get_db),
    ticket_id: int,
) -> Any:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    ticket.status = "resolved"
    ticket.resolved_at = datetime.utcnow()
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket
