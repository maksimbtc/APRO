import pytest
import requests

from base.apibase import route_auth, route_settings, get_json_file
from suite_tests.API.config.header import Header
from base.static_info import LOGIN_CRED, PASSWORD_CRED, NAME_SEPA, IBAN_SEPA, BIC_SEPA


@pytest.fixture(scope="session", autouse=True)
def auth():
    """
    Performs request for Bearer token before pytest session
    :return: dict with Authorization Bearer token
    """
    headers = Header()

    body = {'login': LOGIN_CRED, 'password': PASSWORD_CRED}

    token = requests.post(
        route_auth('login'),
        headers=headers.get_header(),
        json=body
    ).json()["data"]["token"]

    return Header('Bearer ' + token).get_header()


@pytest.fixture(scope="session")
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

    assert response.status_code == 200, 'Bank detail profile was not updated'


@pytest.fixture(scope="session")
def add_working_hours(auth):
    """
    Setup for garage working hours
    :param auth:
    """

    response = requests.put(
        route_settings('put_working_hours'),
        json=get_json_file('put_working_hours.json'),
        headers=auth)

    assert response.status_code == 200, 'Garage working hours ware not updated'
