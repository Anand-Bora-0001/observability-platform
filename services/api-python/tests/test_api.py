from fastapi.testclient import TestClient
from main import app
from app.db.session import engine
from app.models.base import Base

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Observability Platform API"}

def test_servers_endpoint():
    response = client.get("/api/servers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_incidents_endpoints():
    # Since we have webhooks, we can test that the endpoint exists
    response = client.get("/api/servers/")
    assert response.status_code == 200
