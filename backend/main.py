from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, servers, services, webhooks, tickets, sla, maintenance

app = FastAPI(
    title="Observability Platform API",
    description="Enterprise-grade Infrastructure Monitoring & Incident Management Platform",
    version="0.1.0",
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(servers.router, prefix="/api/servers", tags=["servers"])
app.include_router(services.router, prefix="/api/services", tags=["services"])
app.include_router(webhooks.router, prefix="/api/webhooks", tags=["webhooks"])
app.include_router(tickets.router, prefix="/api/tickets", tags=["tickets"])
app.include_router(sla.router, prefix="/api/sla", tags=["sla"])
app.include_router(maintenance.router, prefix="/api/maintenance", tags=["maintenance"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Observability Platform API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
