import pytest
import requests

from base.apibase import route_auth, route_settings
from suite_tests.API.config.header import Header
from suite_tests.API.config.static_info import LOGIN_CRED, PASSWORD_CRED, NAME_SEPA, IBAN_SEPA, BIC_SEPA


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


@pytest.fixture(scope="function")
def add_bank_details(auth):
    """
    Setup for bank details information (alias, iban, bic)
    :param auth:
    """
    body = {
        "alias": NAME_SEPA,
        "iban": IBAN_SEPA,
        "bic": BIC_SEPA
    }

    response = requests.put(
        route_settings('put_bank_detail'),
        json=body,
        headers=auth)

    assert response.status_code == 200, 'Bank detail settings was not updated'
