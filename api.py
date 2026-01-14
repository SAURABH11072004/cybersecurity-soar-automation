from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class IncidentResponse(BaseModel):
    incident_id: str
    type: str
    severity: str
    risk_score: int
    ml_risk_confidence: float
    actions_taken: List[str]
    timestamp: str

@app.get("/incident", response_model=IncidentResponse)
def get_incident():
    return {
        "incident_id": "ALERT-1001",
        "type": "phishing",
        "severity": "high",
        "risk_score": 95,
        "ml_risk_confidence": 99.78,
        "actions_taken": [
            "Blocked phishing sender",
            "Reset user password",
            "Escalated to SOC Tier-2",
            "Assigned to SOC Tier-2"
        ],
        "timestamp": "2026-01-14T08:53:13"
    }
