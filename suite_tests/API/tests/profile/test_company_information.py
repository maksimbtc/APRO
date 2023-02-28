import pytest
import requests

from base.apibase import *


@pytest.mark.Settings
@pytest.mark.API
def test_get_company_name(auth):
    """
    Check company name
    :param auth:
    """
    company_name_response = requests.get(
        route_settings('get_company_info'),
        headers=auth)

    assert company_name_response.status_code == 200, 'Company info service is not available'


@pytest.mark.Settings
@pytest.mark.API
def test_update_company_name(auth):
    """
    Check update company name
    :param auth:
    """
    updated_company_name_response = requests.put(
        route_settings('put_company_information'),
        headers=auth,
        json=get_json_file('put_company_fr.json')
    )
    assert updated_company_name_response.status_code == 200, 'Company info service is not available'

    expected_data = get_json_file('get_company_fr.json')
    actual_data = json.loads(updated_company_name_response.content)

    assert expected_data == actual_data, 'Updated company information data is NOT saved'
