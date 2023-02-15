import pytest
import requests

DOMAIN = 'https://stage-v10.api.autodoc.pro'
LOGIN_CRED = 'test_customer3@autodoc.pro'
PASSWORD_CRED = '12345678'
class Apibase():


    def get_route_auth(get_route: str) -> dict:
        route_name = get_route.lower()
        routeAuth = {
            #POST
            'forgot-password': '/api/auth/forgot-password',
            'login': '/api/auth/login'
        }
        return DOMAIN + routeAuth[route_name]

    def get_route_personal_manager(get_route: str) -> dict:
        route_name = get_route.lower()
        routePM = {
            #GET
            'get_personal_manager': '/api/profile/personal-manager'
        }
        return DOMAIN + routePM[route_name]

    def get_login_credentials(self) -> str:
        return "".join(LOGIN_CRED)

    def get_password_credentials(self) -> str:
        return "".join(PASSWORD_CRED)

    def get_user_token(self) -> str:
        Headers = {"accept": "application/json",
                   "X-COUNTRY-CODE": "FR",
                   "Content-Type": "application/json",
                   "X-CSRF-TOKEN": None
                   }
        body = {'login': LOGIN_CRED, 'password': PASSWORD_CRED}
        response = requests.post(Apibase.get_route_auth('login'), headers=Headers, json=body)
        token = response.json()["data"]["token"]
        return 'Bearer ' + token
