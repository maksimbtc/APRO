import pytest
import requests

from base.apibase import *


@pytest.mark.Settings
@pytest.mark.API
def test_get_working_hours(auth):
    """
    Check the garage working hours
    :param auth:
    """

    response = requests.get(
        route_settings('get_working_hours'),
        headers=auth)

    expected_data = get_json_file('get_working_hours.json')
    actual_data = json.loads(response.content)

    assert response.status_code == 200, 'Working hours is not available'
    assert expected_data == actual_data, 'Working hours were not updated'