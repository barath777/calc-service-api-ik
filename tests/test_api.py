from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_fibonacci_endpoint():
    response = client.get("/fibonacci/10")

    assert response.status_code == 200
    assert response.json() == {"result": 55}


def test_fibonacci_invalid_input():
    response = client.get("/fibonacci/-1")

    assert response.status_code == 400
    assert response.json() == {"detail": "n must be >= 0"}


def test_factorial_endpoint():
    response = client.get("/factorial/5")

    assert response.status_code == 200
    assert response.json() == {"result": 120}


def test_factorial_invalid_input():
    response = client.get("/factorial/-5")

    assert response.status_code == 400
    assert response.json() == {"detail": "n must be >= 0"}


def test_loan_endpoint():
    payload = {"principal": 100000, "annual_rate": 10, "months": 12}
    response = client.post("/loan", json = payload)

    assert response.status_code == 200

    data = response.json()

    assert "monthly_payment" in data
    assert data["monthly_payment"] > 0

def test_loan_zero_interest():
    payload = {"principal": 1200, "annual_rate":0, "months": 12}
    response = client.post("/loan", json=payload)

    assert response.status_code == 200
    assert response.json() == {"monthly_payment": 100.0}


def test_loan_invalid_months():
    payload = {"principal": 10000, "annual_rate":10, "months": 0}
    response = client.post("/loan", json=payload)

    assert response.status_code == 400
    assert response.json() == {
        "detail": "months must be > 0"
    }


def test_loan_negative_interest():
    payload = {"principal": 100000, "annual_rate": -5, "months": 12}
    response = client.post("/loan", json=payload)

    assert response.status_code == 400
    assert response.json() == {
        "detail": "annual_rate must be >= 0"
    }