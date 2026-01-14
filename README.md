# 🚨 Cybersecurity SOAR Automation Platform

A **Security Orchestration, Automation, and Response (SOAR)** platform built using **Python, FastAPI, Machine Learning, Docker**, and deployed on **Railway**.  
This project simulates real-world **Security Operations Center (SOC)** workflows such as incident scoring, escalation, response automation, and API exposure.

---

## 🌐 Live Deployment

- **Swagger UI (API Documentation)**  
  👉 https://cybersecurity-soar-automation-production.up.railway.app/docs

- **Incident API Endpoint**  
  👉 https://cybersecurity-soar-automation-production.up.railway.app/incident

---

## 🧠 Project Overview

This project demonstrates how modern SOC teams automate incident handling:

- 📥 Incident ingestion
- ⚠️ Risk score calculation
- 🤖 ML-based risk confidence using ML models
- 🚨 Escalation decision logic (SOC Tier handling)
- 👤 SOC role assignment
- 📄 Incident logging & reporting
- 🌐 REST API exposure using FastAPI
- ☁️ Cloud deployment using Railway

## 🐳 Docker Setup

![Docker Setup](images/Screenshot%202026-01-14%20145343.png)

---

## ⚙️ Implementation Screenshots

![Implementation 1](images/Screenshot%202026-01-14%20145406.png)

![Implementation 2](images/Screenshot%202026-01-14%20145429.png)

![Implementation 3](images/Screenshot%202026-01-14%20145503.png)

![Implementation 4](images/Screenshot%202026-01-14%20145523.png)



## 🏗️ Project Architecture

```text
📁 cybersecurity-soar-automation
├── api.py                  # FastAPI application exposing SOC incident APIs
├── main.py                 # Core SOAR automation workflow
├── requirements.txt        # Project dependencies
├── Dockerfile              # Docker configuration for containerization
│
├── utils/
│   ├── risk_engine.py      # Rule-based risk scoring logic
│   ├── escalation.py       # SOC escalation decision logic
│   └── role_handler.py     # SOC role & ownership assignment
│
├── ml/
│   └── ml_risk_model.py    # Machine Learning-based risk confidence model
│
├── reports/
│   └── report_generator.py # Incident report generation module
│
├── logs/
│   └── incident_logs.txt   # SOC incident audit logs
│
└── README.md               # Project documentation


---

## ⚙️ Technology Stack

- **Language:** Python  
- **Backend Framework:** FastAPI  
- **Machine Learning:** scikit-learn  
- **API Documentation:** Swagger (OpenAPI)  
- **Containerization:** Docker  
- **Cloud Deployment:** Railway  
- **Version Control:** Git & GitHub  

---

## 🚀 Features

- Automated SOC incident processing
- Risk score calculation using rule-based logic
- ML-driven confidence scoring
- Automatic SOC Tier escalation
- Role-based incident ownership
- Structured logging & reporting
- RESTful API exposure
- Dockerized & cloud-deployed

---

## 🔌 API Details

### `GET /incident`

Returns a simulated SOC incident response.

#### Sample Response
```json
{
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

