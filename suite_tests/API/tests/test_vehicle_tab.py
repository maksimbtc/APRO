import pytest
import requests

from base.apibase import *


@pytest.mark.basket_tab_detlete
@pytest.mark.API
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
