import requests
import unittest
import pytest
from base.apibase import Apibase


class PersonalManager(unittest.TestCase):

    @pytest.mark.personal_manager_api
    def test_get_personal_manager(self):
        Headers = {"accept": "application/json",
                   "Authorization": Apibase.get_user_token(self),
                   "Content-Type": "application/json",
                   "X-CSRF-TOKEN": None
                   }
        response = requests.get(Apibase.get_route_personal_manager('get_personal_manager'), headers=Headers)
        assert response.status_code == 200, 'User has personal manager'

    @pytest.mark.personal_manager_api
    def test_set_personal_manager_rating_without_pm(self):
        Headers = {"accept": None,
                   "Authorization": Apibase.get_user_token(self),
                   "Content-Type": "application/json",
                   "X-CSRF-TOKEN": None
                   }
        body = {"rating": 1, "comment": "Some comment"}
        response = requests.post(Apibase.get_route_personal_manager('set_personal_manager_rating'), headers=Headers,
                                 json=body)
        assert response.status_code == 422, 'User has personal manager'


if __name__ == '__main__':
    unittest.main()
