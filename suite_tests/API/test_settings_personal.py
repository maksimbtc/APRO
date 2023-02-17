import pytest
from suite_tests.API.config.header import Header
from base.apibase import *


def test_update_bank_detail():
    headers = Header(get_user_token())
    body = {
        "alias": NAME_SEPA,
        "iban": IBAN_SEPA,
        "bic": BIC_SEPA
    }

    response = requests.put(
        get_route_settings('put_bank_detail'),
        json=body,
        headers=headers.get_header()
    )

    assert response.status_code == 200, 'Bank detail settings was not updated'
