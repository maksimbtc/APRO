import pytest
import requests

from base.apibase import *
from suite_tests.API.config.header import Header


@pytest.mark.AuthAPI
@pytest.mark.API
def test_authorization():
    headers = Header()
    body = {
        "login": get_login_credentials(),
        "password": get_password_credentials()
    }

    response = requests.post(
        route_auth('login'),
        headers=headers.get_header(),
        json=body)

    assert response.status_code == 200, 'User is NOT authorized'