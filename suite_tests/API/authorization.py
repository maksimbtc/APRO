import requests
import unittest
from base.apibase import Apibase


class authorization(unittest.TestCase):
    def test_authorization(self):
        Headers = {"accept": "application/json",
                   "X-COUNTRY-CODE": "FR",
                   "Content-Type": "application/json",
                   "X-CSRF-TOKEN": None
                   }
        body = {"login": Apibase.get_login_credentials(self), "password": Apibase.get_password_credentials(self)}
        response = requests.post(Apibase.get_route_auth('login'), headers=Headers, json=body)
        assert response.status_code == 200, 'User is authorized'


if __name__ == '__main__':
    unittest.main()
