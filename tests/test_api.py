import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

API_KEY = "smartexpense-key"


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_get_expenses():

    response = client.get("/expenses")

    assert response.status_code == 200


def test_summary():

    response = client.get("/summary")

    assert response.status_code == 200


def test_create_expense():

    expense = {
        "title": "Lunch",
        "amount": 250,
        "category": "Food",
        "description": "Lunch expense"
    }

    response = client.post(
        "/expenses",
        json=expense,
        headers={
            "X-API-Key": API_KEY
        }
    )

    assert response.status_code == 200