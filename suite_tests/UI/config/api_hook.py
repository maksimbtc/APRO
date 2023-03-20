import pytest
import requests

from base.apibase import route_auth, route_settings, get_json_file, route_basket, vehicle_tab
from suite_tests.API.config.header import Header
from base.static_info import LOGIN_CRED, PASSWORD_CRED, NAME_SEPA, IBAN_SEPA, BIC_SEPA


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

def add_working_hours(auth):
    """
    Setup for garage working hours
    :param auth:
    """

    response = requests.put(
        route_settings('put_working_hours'),
        json=get_json_file('put_working_hours.json'),
        headers=auth)

def test_delete_all_vehicle_tabs(auth):
    """
    Check delete all vehicle tabs
    :param auth:
    """

    vehicle_tab_response = requests.get(
        vehicle_tab('get-vehicle-tab'),
        headers=auth)

    assert vehicle_tab_response.status_code == 200

    for tab in vehicle_tab_response.json()["data"]["items"]:
        tab_id = tab["id"]

        vehicle_tab_delete_response = requests.delete(
            vehicle_tab('delete-vehicle-tab', tab_id),
            headers=auth)

        assert vehicle_tab_delete_response.status_code == 204, \
            f"Failed to delete vehicle tab with id {tab_id}. Response code: {vehicle_tab_delete_response.status_code}"

    vehicle_tab_response_after_delete = requests.get(
        vehicle_tab('get-vehicle-tab'),
        headers=auth)

    assert vehicle_tab_response_after_delete.status_code == 200
    assert len(
        vehicle_tab_response_after_delete.json()['data']['items']) == 0, "One or more vehicle tabs were not deleted"