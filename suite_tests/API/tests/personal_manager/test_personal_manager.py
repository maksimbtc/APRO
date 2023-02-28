import pytest
import requests

from base.apibase import *


@pytest.mark.PersonalManagerAPI
@pytest.mark.API
def test_get_personal_manager(auth):
    """
    Check personal manager
    :param auth:
    """
    response = requests.get(
        route_personal_manager('get_personal_manager'),
        headers=auth)

    assert response.status_code == 200, 'User has not personal manager'


@pytest.mark.PersonalManagerAPI
@pytest.mark.API
def test_set_personal_manager_rating_without_pm(auth):
    """
    Check impossibility to rate personal manager without one
    :param auth:
    """
    rating = {"rating": 1, "comment": "comment"}

    response = requests.post(
        route_personal_manager('set_personal_manager_rating'),
        headers=auth,
        json=rating)

    assert response.status_code == 422, 'User has personal manager'
