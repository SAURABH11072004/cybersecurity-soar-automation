import json
from datetime import datetime

def generate_report(incident, actions, risk_score, ml_risk):
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "incident_id": incident["id"],
        "type": incident["type"],
        "severity": incident["severity"],
        "risk_score": risk_score,
        "ml_risk_confidence": ml_risk,
        "actions": actions
    }

    with open("reports/daily_report.json", "w") as f:
        json.dump(report, f, indent=4)
