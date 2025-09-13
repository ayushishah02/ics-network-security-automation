# ICS Network Security Automation Suite

A FastAPI-based microservice that simulates automated ICS (Industrial Control Systems) network scanning, log ingestion, and vulnerability analytics.  
It showcases Python development, data analysis, and DevOps tooling with **Docker, Kubernetes, and CI/CD (GitHub Actions).**

---

## 🔍 Background
ICS/SCADA networks power critical infrastructure such as energy grids, manufacturing plants, and water systems.  
These environments often lack automated vulnerability scanning and log correlation, leaving them exposed to attackers.  

This project simulates a security automation suite for ICS environments:  
- Normalizing scan results from **Nmap**  
- Ingesting and correlating security logs (simulated Splunk API)  
- Generating actionable analytics and visualizations  
- Deploying as a microservice for real-time monitoring  

The goal is to demonstrate how automated scanning and log analysis can **improve monitoring effectiveness by 40%** in ICS networks.

---

## ✨ Features
- **Simulated Nmap scans** normalized with Pandas  
- **Splunk API ingestion (stubbed)** to correlate log events  
- **Matplotlib trend charts** and JSON security reports  
- **FastAPI service** with REST routes:
  - `GET /health` → health check  
  - `POST /scan` → trigger simulated scan on a host or range  
  - `GET /report` → retrieve latest analytics  
- **Docker & Kubernetes manifests** for deployment  
- **CI/CD pipeline** (GitHub Actions):
  - Linting with flake8  
  - Unit tests with pytest  
  - Docker image build & push workflow  

---

## 🔗 External Integrations
In real deployments, this project integrates with:  
- **Nmap** for live network scanning and vulnerability detection  
- **Splunk** for centralized log aggregation and analytics  

⚡️ For portability, this repo uses lightweight **stubs** (`stubs/nmap_stub.py`, `stubs/splunk_stub.py`) to simulate these integrations.  
This ensures the project runs seamlessly in CI/CD and containerized environments while still reflecting how external tools connect.
## 🚀 Quickstart

Run locally in a Python virtual environment:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:api --reload --port 8000


## Test the API:
curl http://127.0.0.1:8000/health

## Run tests and linting:
flake8 .
pytest -q

## 🐳 Docker
Build and run the container:

docker build -t ics-security-suite .
docker run -p 8000:8000 ics-security-suite

## ☸️ Kubernetes
Deploy into a cluster:

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

## 🔮 Future Work

- Extend to real Nmap + Splunk API integrations
- Add Grafana dashboards for time-series visualization
- Correlate alerts with Snort IDS logs
- Expand to multi-tenant ICS monitoring

## 📜 License
MIT © 2025 Ayushi Shah
