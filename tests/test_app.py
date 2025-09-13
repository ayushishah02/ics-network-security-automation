from fastapi.testclient import TestClient
import app

client = TestClient(app.api)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'

def test_scan_and_report():
    r = client.post('/scan', json={'target': '10.0.0.0/24', 'tags': ['ics', 'demo']})
    assert r.status_code == 200
    r2 = client.get('/report')
    assert r2.status_code == 200
    data = r2.json()
    assert 'summary' in data
