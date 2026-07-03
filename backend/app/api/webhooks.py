import json
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.incident import Incident
from app.models.alert import Alert
from app.schemas.incident import AlertmanagerPayload

router = APIRouter()

@router.post("/alertmanager")
async def receive_alertmanager_webhook(
    payload: AlertmanagerPayload,
    db: Session = Depends(get_db)
):
    """
    Receives alerts from Alertmanager and creates/updates Incidents.
    """
    for alert_data in payload.alerts:
        # Create an Incident for firing alerts
        incident = None
        if alert_data.status == "firing":
            # Very basic deduplication based on alert name and fingerprint
            incident = Incident(
                title=f"[{alert_data.labels.get('severity', 'warning').upper()}] {alert_data.labels.get('alertname', 'Unknown Alert')}",
                description=alert_data.annotations.get('description', ''),
                severity=alert_data.labels.get('severity', 'warning'),
                status="open"
            )
            db.add(incident)
            db.commit()
            db.refresh(incident)

        # Store the alert record
        alert_record = Alert(
            alert_name=alert_data.labels.get('alertname', 'Unknown'),
            status=alert_data.status,
            labels=json.dumps(alert_data.labels),
            annotations=json.dumps(alert_data.annotations),
            incident_id=incident.id if incident else None
        )
        db.add(alert_record)
        db.commit()

    return {"message": "Webhook processed successfully"}
