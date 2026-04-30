from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_calculate():
    client = app.test_client()
    response = client.post("/calculate", json={
        "weight": 70,
        "program": "Fat Loss"
    })
    assert response.status_code == 200