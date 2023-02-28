import pytest
import requests

from base.apibase import *


@pytest.mark.Settings
@pytest.mark.API
def test_update_bank_detail(auth):
    """
    Check update bank details (alias, iban, bic)
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
    assert response.json()["data"]["alias"] == NAME_SEPA, 'Incorrect Sepa name'
    assert response.json()["data"]["iban"] == IBAN_SEPA, 'Incorrect Sepa IBAN'
    assert response.json()["data"]["bic"] == BIC_SEPA, 'Incorrect Sepa BIC'


@pytest.mark.Settings
@pytest.mark.API
def test_get_bank_detail(auth, add_bank_details):
    """
    Check
    :param auth:
    """
    response = requests.get(
        route_settings('get_bank_detail'),
        headers=auth
    )

    assert response.status_code == 200, 'Bank details service is not available'
    assert response.json()["data"]["alias"] == NAME_SEPA, 'Incorrect Sepa name'
    assert response.json()["data"]["iban"] == IBAN_SEPA, 'Incorrect Sepa IBAN'
    assert response.json()["data"]["bic"] == BIC_SEPA, 'Incorrect Sepa BIC'


@pytest.mark.Settings
@pytest.mark.API
def test_delete_bank_detail(auth, add_bank_details):
    """
    Check deleting bank detail information (alias, iban, bic)
    :param auth:
    """

    deleted_bank_details_response = requests.delete(
        route_settings('delete_bank_detail'),
        headers=auth
    )

    empty_bank_details = requests.get(
        route_settings('get_bank_detail'),
        headers=auth
    ).json()["data"]

    assert deleted_bank_details_response.status_code == 204, 'Bank details was not deleted'
    assert empty_bank_details["alias"] == "", 'Incorrect Sepa name'
    assert empty_bank_details["iban"] == "", 'Incorrect Sepa IBAN'
    assert empty_bank_details["bic"] == "", 'Incorrect Sepa BIC'


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
@pytest.mark.test
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
    print(get_json_file('put_company_fr.json'))
    assert updated_company_name_response.status_code == 200, updated_company_name_response.text

    expected_data = get_json_file('get_company_fr.json')
    actual_data = json.loads(updated_company_name_response.content)

    assert expected_data == actual_data, 'Updated company information data is NOT saved'