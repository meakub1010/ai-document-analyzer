from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize():
    response = client.post("/summarize/", json={"text": "This is the summary of a long file"})
    assert response.status_code == 200
    assert "summary" in response.json()