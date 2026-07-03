import os
import sys
from sqlalchemy.orm import Session

# Add backend to Python path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.session import SessionLocal
from app.models.user import User
from app.models.server import Server
from app.models.service import Service
from app.models.incident import Incident
from app.models.ticket import Ticket
from app.core.security import get_password_hash

def seed_database():
    db: Session = SessionLocal()

    print("Seeding database...")

    # Create admin user if not exists
    admin_user = db.query(User).filter(User.email == "admin@example.com").first()
    if not admin_user:
        admin_user = User(
            email="admin@example.com",
            hashed_password=get_password_hash("adminpassword"),
            full_name="System Admin",
            is_active=True,
            is_superuser=True
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        print("Created admin user.")

    # Create sample servers
    if db.query(Server).count() == 0:
        servers = [
            Server(hostname="web-prod-01", ip_address="10.0.0.10", os_type="Linux", status="active"),
            Server(hostname="db-prod-01", ip_address="10.0.0.11", os_type="Linux", status="active"),
            Server(hostname="cache-01", ip_address="10.0.0.12", os_type="Linux", status="active"),
            Server(hostname="win-util-01", ip_address="10.0.0.20", os_type="Windows", status="maintenance"),
        ]
        db.add_all(servers)
        db.commit()
        for s in servers:
            db.refresh(s)
        print(f"Created {len(servers)} servers.")

        # Create services for the first server
        web_server = servers[0]
        services = [
            Service(name="nginx", server_id=web_server.id, port=80, service_type="HTTP", status="active"),
            Service(name="gunicorn", server_id=web_server.id, port=8000, service_type="App", status="active"),
        ]
        db.add_all(services)
        db.commit()
        print("Created sample services.")

    # Create sample incidents and tickets
    if db.query(Incident).count() == 0:
        incident = Incident(
            title="[CRITICAL] High Memory Usage on db-prod-01",
            description="Memory usage spiked to 95%.",
            severity="critical",
            status="investigating"
        )
        db.add(incident)
        db.commit()
        db.refresh(incident)
        print("Created sample incident.")

        ticket = Ticket(
            title="Investigate memory leak on production database",
            description="Linked to active incident. Need to check Postgres logs.",
            priority="high",
            status="open",
            assignee_id=admin_user.id,
            incident_id=incident.id
        )
        db.add(ticket)
        db.commit()
        print("Created sample ticket.")

    db.close()
    print("Seeding completed successfully.")

if __name__ == "__main__":
    seed_database()
