import requests
import unittest
from base.apibase import Apibase


class PersonalManager(unittest.TestCase):
    def test_get_personal_manager(self):
        Headers = {"accept": "application/json",
                   "Authorization": Apibase.get_user_token(self),
                   "Content-Type": "application/json",
                   "X-CSRF-TOKEN": None
                   }
        response = requests.get(Apibase.get_route_personal_manager('get_personal_manager'), headers=Headers)
        assert response.status_code == 200, 'User has personal manager'

if __name__ == '__main__':
    unittest.main()
