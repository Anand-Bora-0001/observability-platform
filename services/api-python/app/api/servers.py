from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.server import Server
from app.schemas.server import ServerCreate, ServerResponse, ServerUpdate

router = APIRouter()

@router.post("/", response_model=ServerResponse)
def create_server(
    *,
    db: Session = Depends(get_db),
    server_in: ServerCreate,
) -> Any:
    server = db.query(Server).filter(Server.hostname == server_in.hostname).first()
    if server:
        raise HTTPException(status_code=400, detail="Server with this hostname already exists")
    server = Server(**server_in.model_dump())
    db.add(server)
    db.commit()
    db.refresh(server)
    return server

@router.get("/", response_model=List[ServerResponse])
def read_servers(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    servers = db.query(Server).offset(skip).limit(limit).all()
    return servers

@router.get("/{server_id}", response_model=ServerResponse)
def read_server(
    *,
    db: Session = Depends(get_db),
    server_id: int,
) -> Any:
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server
