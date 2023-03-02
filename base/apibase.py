import json
import os
from base.static_info import *


def put_basket(route: str, product_id: str) -> str:
    route_name = route.lower()
    routes = {
        # PUT
        'basket-alternative-id': f'/api/basket-product/{product_id}/alternative'
    }
    return DOMAIN + routes[route_name]


def route_basket(route: str) -> str:
    route_name = route.lower()
    routes = {
        # GET
        'get-basket': '/api/basket',
        # DELETE basket-tab
        'delete-basket-tab': '/api/basket-tab/',
        # POST basket-product
        'post-product': '/api/basket-product',
        # PUT basket-product/{id}
        'basket-product-id': '/api/basket-product/'
    }
    return DOMAIN + routes[route_name]

def route_personal_manager(route: str) -> str:
    route_name = route.lower()
    routes = {
        # GET
        'get_personal_manager': '/api/profile/personal-manager',

        # POST
        'set_personal_manager_rating': '/api/profile/personal-manager/rating'
    }
    return DOMAIN + routes[route_name]


def route_settings(route: str) -> str:
    route_name = route.lower()
    routes = {
        # GET
        'get_bank_detail': '/api/settings/bank-detail',
        'get_company_info': '/api/settings/company',
        'get_working_hours': '/api/settings/working-hours',

        # PUT
        'put_bank_detail': '/api/settings/bank-detail',
        'put_company_information': '/api/settings/company',
        'put_working_hours': '/api/settings/working-hours',

        # DELETE
        'delete_bank_detail': '/api/settings/bank-detail'
    }
    return DOMAIN + routes[route_name]


def get_login_credentials() -> str:
    return "".join(LOGIN_CRED)


def get_password_credentials() -> str:
    return "".join(PASSWORD_CRED)


def get_json_file(file_name):
    path = os.path.join('suite_tests', 'API', 'config', 'resources', file_name)
    with open(path, 'r', encoding='utf-8') as f:
        json_object = json.load(f)

    return json_object
