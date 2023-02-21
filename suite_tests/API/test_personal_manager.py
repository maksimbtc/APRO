import pytest

from base.apibase import *
from suite_tests.API.config.header import Header


@pytest.mark.PersonalManagerAPI
@pytest.mark.API
def test_get_personal_manager():
    headers = Header(get_user_token())

    response = requests.get(
        get_route_personal_manager('get_personal_manager'),
        headers=headers.get_header()
    )

    assert response.status_code == 200, 'User has personal manager'


@pytest.mark.PersonalManagerAPI
@pytest.mark.API
def test_set_personal_manager_rating_without_pm():
    headers = Header(get_user_token())

    body = {"rating": 1, "comment": "Some comment"}

    response = requests.post(
        get_route_personal_manager('set_personal_manager_rating'),
        headers=headers.get_header(),
        json=body
    )

    assert response.status_code == 422, 'User has personal manager'
