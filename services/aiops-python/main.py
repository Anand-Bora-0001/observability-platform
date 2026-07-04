from fastapi import FastAPI
from app.api import analyze
from app.services.kafka_consumer import run_consumer_in_background

app = FastAPI(
    title="AI Ops Service",
    description="LLM-assisted Root Cause Analysis and Operations",
    version="0.1.0"
)

@app.on_event("startup")
def startup_event():
    run_consumer_in_background()

app.include_router(analyze.router, prefix="/api/ai", tags=["ai"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
