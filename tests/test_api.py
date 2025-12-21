import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_predict():
    payload = {
        "longitude": -122.23,
        "latitude": 37.88,
        "housing_median_age": 41,
        "total_rooms": 880,
        "total_bedrooms": 129,
        "population": 322,
        "households": 126,
        "median_income": 8.3252,
        "rooms_per_household": 7.0,
        "bedrooms_per_room": 0.15,
        "population_per_household": 2.5,
        "ocean_proximity": "NEAR OCEAN"
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json()
