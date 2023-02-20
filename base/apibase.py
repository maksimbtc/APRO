import requests

from suite_tests.API.config.header import Header
from suite_tests.API.config.statis_info import *


def get_route_auth(route: str) -> str:
    route_name = route.lower()
    routeAuth = {
        # POST
        'forgot-password': '/api/auth/forgot-password',
        'login': '/api/auth/login'
    }
    return DOMAIN + routeAuth[route_name]


def get_route_personal_manager(route: str) -> str:
    route_name = route.lower()
    routePM = {
        # GET
        'get_personal_manager': '/api/profile/personal-manager',

        # POST
        'set_personal_manager_rating': '/api/profile/personal-manager/rating'
    }
    return DOMAIN + routePM[route_name]


def get_route_settings(route: str) -> str:
    route_name = route.lower()
    routePM = {
        # PUT
        'put_bank_detail': '/api/settings/bank-detail'
    }
    return DOMAIN + routePM[route_name]


def get_login_credentials() -> str:
    return "".join(LOGIN_CRED)


def get_password_credentials() -> str:
    return "".join(PASSWORD_CRED)


def get_user_token() -> str:
    headers = Header()

    body = {'login': LOGIN_CRED, 'password': PASSWORD_CRED}

    response = requests.post(
        get_route_auth('login'),
        headers=headers.get_header(),
        json=body
    )

    token = response.json()["data"]["token"]

    return 'Bearer ' + token
