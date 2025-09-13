# ICS Network Security Automation Suite

A FastAPI microservice that **simulates** automated ICS network scanning, log ingestion, and vulnerability analytics.  
It showcases Python, Docker, Kubernetes, and CI/CD with GitHub Actions.

---

## ✨ Features
- Orchestrates simulated Nmap scans and normalizes results with Pandas.
- Ingests (mock) Splunk logs via an API client and correlates with scan findings.
- Generates Matplotlib trend charts and JSON reports.
- Exposes routes via FastAPI:
  - `GET /health`
  - `POST /scan` (target range or host)
  - `GET /report` (latest analytics)
- Includes Dockerfile + Kubernetes Deployment & Service.
- CI pipeline runs lint & tests; builds Docker image (push step left as a comment).

> **Note:** This project **simulates** scanning/log ingestion for safety, so you can run it anywhere.

---

## 🚀 Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:api --reload --port 8000
