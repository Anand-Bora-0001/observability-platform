from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class AlertPayload(BaseModel):
    alert_name: str
    severity: str
    description: str
    labels: dict

class RCAResponse(BaseModel):
    root_cause_hypothesis: str
    recommended_actions: List[str]
    similar_past_incidents: List[str]

@router.post("/rca", response_model=RCAResponse)
def perform_rca(alert: AlertPayload):
    """
    Mock implementation of LLM-based Root Cause Analysis.
    In a real system, this would:
    1. Query a Vector Database (Pinecone, Weaviate) for past similar alerts (RAG).
    2. Pass the alert + past context to Langchain / OpenAI.
    3. Return structured JSON recommendations.
    """
    
    # Mock RAG retrieval
    past_incidents = [
        "INC-1042: High CPU on auth-service causing cascading timeouts (Resolved: Scaled replicas)",
        "INC-991: Database connection pool exhaustion (Resolved: Increased max_connections)"
    ]
    
    # Mock LLM generation
    if "CPU" in alert.description.upper() or "LOAD" in alert.description.upper():
        hypothesis = "Likely a traffic spike causing resource starvation on the node."
        actions = [
            "Check current horizontal pod autoscaler (HPA) limits.",
            "Verify if a recent deployment introduced a CPU regression.",
            "Inspect container resource requests and limits in Kubernetes."
        ]
    else:
        hypothesis = "Potential configuration error or upstream service degradation."
        actions = [
            "Check logs for FATAL or ERROR level messages.",
            "Verify network connectivity and DNS resolution.",
            "Review recent commits in the infrastructure repository."
        ]

    return RCAResponse(
        root_cause_hypothesis=hypothesis,
        recommended_actions=actions,
        similar_past_incidents=past_incidents
    )

class RunbookRequest(BaseModel):
    incident_description: str

class RunbookResponse(BaseModel):
    runbook_steps: List[str]

@router.post("/runbook", response_model=RunbookResponse)
def generate_runbook(req: RunbookRequest):
    """
    Mock implementation of LLM Runbook Generation.
    """
    steps = [
        "1. Acknowledge the alert in the NOC dashboard.",
        "2. Check the logs in Loki for the affected service.",
        "3. Review recent deployments in the CI/CD pipeline.",
        "4. If CPU is exhausted, manually scale the deployment replicas."
    ]
    return RunbookResponse(runbook_steps=steps)

class LogExplanationRequest(BaseModel):
    log_snippet: str

class LogExplanationResponse(BaseModel):
    explanation: str
    severity_assessment: str

@router.post("/explain-log", response_model=LogExplanationResponse)
def explain_log(req: LogExplanationRequest):
    """
    Mock Natural Language Log Explanation.
    """
    return LogExplanationResponse(
        explanation=f"The log '{req.log_snippet}' indicates a failure in the downstream connection pool.",
        severity_assessment="High - Immediate attention required."
    )
