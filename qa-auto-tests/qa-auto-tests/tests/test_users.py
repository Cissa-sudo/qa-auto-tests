from utils.api_client import get_users, get_user


def test_get_users_list():
    response = get_users()

    assert response.status_code == 200
    data = response.json()

    assert "data" in data
    assert len(data["data"]) > 0


def test_get_single_user():
    response = get_user(2)

    assert response.status_code == 200
    data = response.json()

    assert data["data"]["id"] == 2
    assert "email" in data["data"]

