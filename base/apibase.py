import pytest
import requests

DOMAIN = 'https://stage-v10.api.autodoc.pro'
class Apibase():


    def get_route_auth(get_route: str) -> dict:
        route_name = get_route.lower()
        routeAuth = {
            'forgot-password': '/api/auth/forgot-password',
            'login': '/api/auth/login'
        }
        return DOMAIN + routeAuth[route_name]