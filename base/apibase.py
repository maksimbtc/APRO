import pytest
import requests

DOMAIN = 'https://stage-v10.api.autodoc.pro'
LOGIN_CRED = 'test_customer3@autodoc.pro'
PASSWORD_CRED = '12345678'
class Apibase():


    def get_route_auth(get_route: str) -> dict:
        route_name = get_route.lower()
        routeAuth = {
            'forgot-password': '/api/auth/forgot-password',
            'login': '/api/auth/login'
        }
        return DOMAIN + routeAuth[route_name]

    def get_login_credentials(self) -> str:
        return "".join(LOGIN_CRED)

    def get_password_credentials(self) -> str:
        return "".join(PASSWORD_CRED)
