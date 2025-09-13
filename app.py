from fastapi import FastAPI, Body
from pydantic import BaseModel
import pandas as pd
import matplotlib.pyplot as plt
import io, base64, time, random
from typing import List, Optional

SCAN_RESULTS = []
SPLUNK_LOGS = []
LATEST_REPORT = {}

api = FastAPI(title="ICS Network Security Automation Suite")

class ScanRequest(BaseModel):
    target: str
    tags: Optional[List[str]] = None

def simulate_nmap_scan(target: str):
    random.seed(hash(target) % 2**32)
    hosts = []
    for i in range(15):
        host = {
            "host": f"10.0.0.{i+10}",
            "port": random.choice([22, 80, 443, 502, 8080, 1883]),
            "service": random.choice(["ssh", "http", "https", "modbus", "http-alt", "mqtt"]),
            "state": random.choice(["open", "filtered", "closed"]),
            "cvss": round(random.uniform(3.5, 9.8), 1)
        }
        hosts.append(host)
    return hosts

def fetch_mock_splunk_logs():
    now = int(time.time())
    records = []
    for i in range(30):
        records.append({
            "ts": now - i * 60,
            "src": f"10.0.0.{random.randint(10,30)}",
            "sig": random.choice(["SCAN_SYN_FLOOD", "MODBUS_ANOMALY", "HTTP_DIR_TRAVERSAL", "MQTT_BRUTE"]),
            "severity": random.choice(["low", "medium", "high"])
        })
    return records

def build_report():
    df_scan = pd.DataFrame(SCAN_RESULTS)
    df_logs = pd.DataFrame(SPLUNK_LOGS)
    summary = {}
    if not df_scan.empty:
        summary["top_services"] = df_scan["service"].value_counts().to_dict()
        summary["high_risk_hosts"] = df_scan[df_scan["cvss"] >= 7.0].groupby("host").size().sort_values(ascending=False).head(5).to_dict()
    if not df_logs.empty:
        summary["alert_counts"] = df_logs["sig"].value_counts().to_dict()
        summary["severity_counts"] = df_logs["severity"].value_counts().to_dict()

    chart_png = None
    if not df_logs.empty:
        grouped = df_logs.groupby("ts").size().sort_index()
        plt.figure()
        grouped.plot(kind="line", marker="o", title="Alert Volume Over Time")
        plt.xlabel("Epoch (s)")
        plt.ylabel("Alerts")
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        chart_png = base64.b64encode(buf.read()).decode("utf-8")

    return {"summary": summary, "chart_png": chart_png}

@api.get("/health")
def health():
    return {"status": "ok"}

@api.post("/scan")
def run_scan(req: ScanRequest = Body(...)):
    hosts = simulate_nmap_scan(req.target)
    for h in hosts:
        h["target"] = req.target
        h["tags"] = req.tags or []
    SCAN_RESULTS.extend(hosts)
    global SPLUNK_LOGS
    SPLUNK_LOGS = fetch_mock_splunk_logs()
    global LATEST_REPORT
    LATEST_REPORT = build_report()
    return {"inserted": len(hosts), "target": req.target}

@api.get("/report")
def get_report():
    return LATEST_REPORT or build_report()
