from datetime import datetime
import os

from utils.risk_engine import calculate_risk_score
from utils.escalation import should_escalate
from utils.role_handler import assign_owner
from ml.ml_risk_model import ml_risk_prediction
from reports.report_generator import generate_report

# Ensure log directory exists
os.makedirs("logs", exist_ok=True)

incident = {
    "id": "ALERT-1001",
    "type": "phishing",
    "severity": "high",
    "indicators": [
        "suspicious_link",
        "spoofed_sender",
        "malicious_attachment"
    ],
    "user": "employee1@company.com"
}

risk_score = calculate_risk_score(
    incident["severity"],
    len(incident["indicators"])
)

ml_risk = ml_risk_prediction(
    len(incident["indicators"]),
    risk_score
)

actions = [
    f"Blocked phishing sender for {incident['user']}",
    "Reset user password",
    "Flagged email for forensic analysis",
    "User security awareness notification sent"
]

if should_escalate(risk_score):
    actions.append("Incident escalated to SOC Tier-2")

owner = assign_owner(incident["severity"])
actions.append(f"Assigned to {owner}")

print("\n--- SOC INCIDENT NOTIFICATION ---")
print(f"Incident ID: {incident['id']}")
print(f"Type: {incident['type']}")
print(f"Severity: {incident['severity']}")
print(f"Risk Score: {risk_score}")
print(f"ML Risk Confidence: {ml_risk}%")
print(f"Actions Taken: {actions}")
print(f"Timestamp: {datetime.utcnow().isoformat()}")
print("--------------------------------\n")

with open("logs/incident_logs.txt", "a") as log:
    log.write(f"{incident['id']} | {risk_score} | {ml_risk}% | {datetime.utcnow()}\n")

generate_report(incident, actions, risk_score, ml_risk)
