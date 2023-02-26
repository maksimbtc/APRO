import pytest
from base.apibase import *
import math


@pytest.mark.recalculation_basket
@pytest.mark.API
def test_recalculation_basket(auth):
    """
    Check recalculation price for all products
    :param auth:
    """
    basket_response = requests.get(
        route_basket('get-basket'),
        headers=auth)

    assert basket_response.status_code == 200

    tabs = basket_response.json()["data"]["tabs"]
    for tab in tabs:
        products = tab["products"]

        for product in products:
            price_non_vat = round(product["priceNonVat"]["value"], 2)
            quantity = round(product["quantity"]["value"], 2)
            price_total = round(product["priceTotal"]["value"], 2)

            print(f"price_non_vat: {price_non_vat}, quantity: {quantity}, price_total: {price_total}")

            assert math.isclose(price_total, price_non_vat * quantity, rel_tol=1e-9, abs_tol=0.0)

    total_price = round(basket_response.json()["data"]["totalPrice"]["value"], 2)
    calculated_total_price = round(sum([sum([product["priceTotal"]["value"]
                                             for product in tab["products"]]) for tab in tabs]), 2)

    print(f"total_price: {total_price}, calculated_total_price: {calculated_total_price}")

    assert math.isclose(total_price, calculated_total_price, rel_tol=1e-9, abs_tol=0.0)
