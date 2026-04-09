import pytest
from utils.api_client import login


def test_login_success():
    response = login("eve.holt@reqres.in", "cityslicka")

    assert response.status_code == 200
    assert "token" in response.json()


def test_login_without_password():
    response = login("peter@klaven", "")

    assert response.status_code == 400
    assert "error" in response.json()

