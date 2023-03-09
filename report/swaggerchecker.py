import requests
import json
from base.static_info import SWAGGER_DOMAIN
from jinja2 import Template


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

# Список покрытых тестами роутов и методов
covered_routes = {
    '/api/auth/login': ['post'],
    '/api/basket-product/{id}/alternative': ['put'],
    '/api/basket': ['get', 'put'],
    '/api/basket-tab/{id}': ['put', 'delete'],
    '/api/basket-product': ['post'],
    '/api/basket-product/{id}': ['put', 'delete'],
    '/api/profile/personal-manager': ['get'],
    '/api/profile/personal-manager/rating': ['post'],
    '/api/settings/bank-detail': ['get', 'put', 'delete'],
    '/api/settings/company': ['get', 'put'],
    '/api/settings/working-hours': ['get', 'put']
}

covered = []
uncovered = []

for i in range(len(keys)):
    route = keys[i]
    route_methods = methods[i]
    if route in covered_routes.keys():
        for method in route_methods:
            if method.lower() in covered_routes[route]:
                covered.append(f"{route} ({method.lower()})")
            else:
                uncovered.append(f"{route} ({method.lower()})")
    else:
        uncovered.extend([f"{route} ({method.lower()})" for method in route_methods])

total_routes = len(covered) + len(uncovered)
coverage_percentage = len(covered) / total_routes * 100
total = round(coverage_percentage, 2)

print("Covered routes:")
for route in covered:
    print(route)

print("\nUncovered routes:")
for route in uncovered:
    print(route)
with open('template.html') as f:
    template = Template(f.read())

html = template.render(covered=covered, uncovered=uncovered, total=total)

with open('output.html', 'w') as f:
    f.write(html)