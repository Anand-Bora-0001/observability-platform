import json
from datetime import datetime
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.incident import Incident
from app.models.alert import Alert
from app.models.server import Server
from app.models.maintenance_window import MaintenanceWindow
from app.schemas.incident import AlertmanagerPayload

router = APIRouter()

@router.post("/alertmanager")
async def receive_alertmanager_webhook(
    payload: AlertmanagerPayload,
    db: Session = Depends(get_db)
):
    """
    Receives alerts from Alertmanager, checks for maintenance windows, and creates/updates Incidents.
    """
    now = datetime.utcnow()

    for alert_data in payload.alerts:
        # Check if the alert maps to a specific server instance
        instance = alert_data.labels.get('instance')
        server = None
        if instance:
            # Attempt to find server by IP or hostname (instance usually includes port, e.g. 10.0.0.10:9100)
            host = instance.split(':')[0]
            server = db.query(Server).filter(
                (Server.ip_address == host) | (Server.hostname == host)
            ).first()

        # Check for active maintenance windows
        is_in_maintenance = False
        if server:
            active_window = db.query(MaintenanceWindow).filter(
                MaintenanceWindow.is_active == True,
                MaintenanceWindow.start_time <= now,
                MaintenanceWindow.end_time >= now,
                (MaintenanceWindow.server_id == server.id) | (MaintenanceWindow.server_id == None)
            ).first()
            if active_window:
                is_in_maintenance = True

        # Create an Incident only if firing AND not in maintenance
        incident = None
        if alert_data.status == "firing" and not is_in_maintenance:
            incident = Incident(
                title=f"[{alert_data.labels.get('severity', 'warning').upper()}] {alert_data.labels.get('alertname', 'Unknown Alert')}",
                description=alert_data.annotations.get('description', ''),
                severity=alert_data.labels.get('severity', 'warning'),
                status="open"
            )
            db.add(incident)
            db.commit()
            db.refresh(incident)

        # Always store the alert record for auditing, even during maintenance
        alert_record = Alert(
            alert_name=alert_data.labels.get('alertname', 'Unknown'),
            status="suppressed" if (alert_data.status == "firing" and is_in_maintenance) else alert_data.status,
            labels=json.dumps(alert_data.labels),
            annotations=json.dumps(alert_data.annotations),
            incident_id=incident.id if incident else None
        )
        db.add(alert_record)
        db.commit()

    return {"message": "Webhook processed successfully"}
