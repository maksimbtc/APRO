import requests
import json

SWAGGER_DOMAIN = 'https://stage-v10.api.autodoc.pro/api/docs/version/v10'


def get_keys_and_methods_by_prefix(data, prefix):
    paths = data.get('paths', {})
    keys = []
    methods = []
    for key in paths.keys():
        if key.startswith(prefix):
            keys.append(key)
            methods.append(list(paths[key].keys()))
    return keys, methods

response = requests.get(SWAGGER_DOMAIN)
data = json.loads(response.content)
prefix = "/api/"

keys, methods = get_keys_and_methods_by_prefix(data, prefix)

# список покрытых тестами роутов и методов
covered_routes = {
    '/api/auth/login': ['post'],
    '/api/basket-product/{id}/alternative': ['put'],
    '/api/basket': ['get'],
    '/api/basket-tab/{id}': ['delete'],
    '/api/basket-product': ['post'],
    '/api/basket-product/{id}': ['put'],
    '/api/profile/personal-manager': ['get'],
    '/api/profile/personal-manager/rating': ['post'],
    '/api/settings/bank-detail': ['get'],
    '/api/settings/company': ['get'],
    '/api/settings/working-hours': ['get'],
    '/api/settings/bank-detail': ['put'],
    '/api/settings/company': ['put'],
    '/api/settings/working-hours': ['put'],
    '/api/settings/bank-detail': ['delete']
}

covered = []
uncovered = []

for i in range(len(keys)):
    route = keys[i]
    route_methods = methods[i]
    if route in covered_routes:
        for method in route_methods:
            if method in covered_routes[route]:
                covered.append(f"{route} ({method})")
            else:
                uncovered.append(f"{route} ({method})")
    else:
        uncovered.extend([f"{route} ({method})" for method in route_methods])

print("Covered routes:")
for route in covered:
    print(route)

print("\nUncovered routes:")
for route in uncovered:
    print(route)