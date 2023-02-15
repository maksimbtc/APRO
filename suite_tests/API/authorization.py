import requests
import unittest

class authorization(unittest.TestCase):
        def test_authorization(self):
            Headers = { "accept": "application/json",
                        "X-COUNTRY-CODE": "FR",
                        "Content-Type": "application/json",
                        "X-CSRF-TOKEN": None
                        }
            body = {"login": "test_customer3@autodoc.pro", "password": "12345678"}
            response = requests.post("https://stage-v10.api.autodoc.pro/api/auth/login", headers= Headers, json=body)
            print(response.text)
            assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()