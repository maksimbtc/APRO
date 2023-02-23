import pytest
from base.apibase import *
import math

headers = Header(get_user_token())


@pytest.mark.recalculation_basket
@pytest.mark.API
def test_recalculation_basket():
    get_response = requests.get(get_route_basket('get-basket'),
                                headers=headers.get_header()
                                )
    assert get_response.status_code == 200
    tabs = get_response.json()["data"]["tabs"]
    for tab in tabs:
        products = tab["products"]
        for product in products:
            price_non_vat = round(product["priceNonVat"]["value"], 2)
            quantity = round(product["quantity"]["value"], 2)
            price_total = round(product["priceTotal"]["value"], 2)
            print(f"price_non_vat: {price_non_vat}, quantity: {quantity}, price_total: {price_total}")
            assert math.isclose(price_total, price_non_vat * quantity, rel_tol=1e-9, abs_tol=0.0)
    total_price = round(get_response.json()["data"]["totalPrice"]["value"], 2)
    calculated_total_price = round(sum([sum([product["priceTotal"]["value"]
                                             for product in tab["products"]]) for tab in tabs]), 2)
    print(f"total_price: {total_price}, calculated_total_price: {calculated_total_price}")
    assert math.isclose(total_price, calculated_total_price, rel_tol=1e-9, abs_tol=0.0)
