from fastapi.testclient import TestClient

import app

client = TestClient(app.api)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_scan_and_report():
    payload = {"target": "10.0.0.0/24", "tags": ["ics", "demo"]}
    resp_scan = client.post("/scan", json=payload)
    assert resp_scan.status_code == 200

    resp_report = client.get("/report")
    assert resp_report.status_code == 200
    data = resp_report.json()
    assert "summary" in data
