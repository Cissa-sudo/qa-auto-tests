from utils.api_client import get_user


def test_user_not_found():
    response = get_user(9999)

    assert response.status_code == 404

