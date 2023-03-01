import pytest
import requests

from base.apibase import *
from .test_basket_recalculation import test_recalculation_basket


@pytest.mark.basket_tab_detlete
@pytest.mark.API
def test_delete_baskets_tabs(auth):
    """
    Check delete all basket tabs
    :param auth:
    """
    basket_response = requests.get(
        route_basket('get-basket'),
        headers=auth)

    assert basket_response.status_code == 200

    tabs = basket_response.json()["data"]["tabs"]
    for tab in tabs:
        tab_id = tab["id"]

        basket_delete_response = requests.delete(
            f"{route_basket('delete-basket-tab')}{tab_id}",
            headers=auth)

        assert basket_delete_response.status_code == 204, \
            f"Failed to delete tab with id {tab_id}. Response code: {basket_delete_response.status_code}"

    basket_response_after_delete = requests.get(
        route_basket('get-basket'),
        headers=auth)

    deleted_basket_tabs_length = len(basket_response_after_delete.json()['data']['tabs'])

    assert basket_response_after_delete.status_code == 200
    assert deleted_basket_tabs_length == 0, "One or more basket were not deleted"


@pytest.mark.add_product_basket
@pytest.mark.API
def test_add_product_basket(auth):
    """
    Check adding product to basket
    :param auth:
    """
    product = {
        "vehicleId": 142911,
        "tabType": 2,
        "articleId": 14644872,
        "quantity": 2
    }
    added_basket_product_response = requests.post(
        route_basket('post-product'),
        json=product,
        headers=auth)

    assert added_basket_product_response.status_code == 204, "Product was not added"

    test_recalculation_basket(auth)


@pytest.mark.add_product_basket
@pytest.mark.API
def test_change_qty_basket(auth):
    """
    Check updating product quantity
    :param auth:
    """
    basket_response = requests.get(
        route_basket('get-basket'),
        headers=auth)

    assert basket_response.status_code == 200

    product_id = basket_response.json()["data"]["tabs"][0]["products"][0]["id"]
    body = {
        "isActive": True,
        "quantity": 10
    }
    basket_product_update = requests.put(
        f"{route_basket('basket-product-id')}{product_id}",
        headers=auth,
        json=body)

    assert basket_product_update.status_code == 200

    updated_product_quantity = requests.get(
        route_basket('get-basket'),
        headers=auth
    ).json()["data"]["tabs"][0]["products"][0]["quantity"]["value"]

    assert updated_product_quantity == 10, "Updated product quantity is invalid"

    test_recalculation_basket(auth)


@pytest.mark.add_product_basket
@pytest.mark.API
def test_alternative_basket(auth):
    """
    Check updated alternative basket
    :param auth:
    """
    basket_response = requests.get(
        route_basket('get-basket'),
        headers=auth)

    assert basket_response.status_code == 200

    product_id = basket_response.json()["data"]["tabs"][0]["products"][0]["id"]
    article_id = {
        "articleId": 7789938
    }
    put_response = requests.put(
        put_basket('basket-alternative-id', product_id),
        headers=auth,
        json=article_id)

    assert put_response.status_code == 200

    product_id_updated = requests.get(
        route_basket('get-basket'),
        headers=auth
    ).json()["data"]["tabs"][0]["products"][0]["id"]

    assert product_id_updated != product_id, "Updated product id is not correct"


@pytest.mark.all_checkbox
@pytest.mark.API
def test_all_checkbox_basket(auth):
    """
    Check updated alternative basket
    :param auth:
    """
    basket_response = requests.get(
        route_basket('get-basket'),
        headers=auth)

    assert basket_response.status_code == 200

    body = {
        "selected": "empty"
    }
    put_response = requests.put(
        route_basket(
            'get-basket'),
        headers=auth,
        json=body)

    assert put_response.status_code == 200


@pytest.mark.tab_checkbox
@pytest.mark.API
def test_tab_checkbox_basket(auth):
    """
    Check updated alternative basket
    :param auth:
    """
    basket_response = requests.get(
        route_basket('get-basket'),
        headers=auth)

    assert basket_response.status_code == 200
    tab = basket_response.json()["data"]["tabs"][0]["id"]
    body = {
        "selected": "all"
    }
    put_response = requests.put(
        put_basket_checkbox('basket-checkbox-id', tab),
        headers=auth,
        json=body)

    assert put_response.status_code == 200
    print(put_response.text)
