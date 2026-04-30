import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ACEest_Fitness import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_calculate():
    client = app.test_client()
    response = client.post('/calculate', json={
        "weight": 70,
        "program": "Fat Loss (FL)"
    })
    assert response.status_code == 200