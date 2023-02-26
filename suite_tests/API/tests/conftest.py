import pytest
import requests

from base.apibase import route_auth
from suite_tests.API.config.header import Header
from suite_tests.API.config.static_info import LOGIN_CRED, PASSWORD_CRED


@pytest.fixture(scope="session", autouse=True)
def auth():
    """
    Performs request for Bearer token before pytest session
    :return: dict with Authorization Bearer token
    """
    print("--- in auth ---")
    headers = Header()

    body = {'login': LOGIN_CRED, 'password': PASSWORD_CRED}

    token = requests.post(
        route_auth('login'),
        headers=headers.get_header(),
        json=body
    ).json()["data"]["token"]

    return Header('Bearer ' + token).get_header()
