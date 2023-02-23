import pytest
from base.apibase import *


headers = Header(get_user_token())


@pytest.mark.basket_tab_detlete
@pytest.mark.API
def test_delete_baskets_tabs():
    get_response = requests.get(get_route_basket('get-basket'),
                                headers=headers.get_header()
                                )
    assert get_response.status_code == 200
    tabs = get_response.json()["data"]["tabs"]
    for tab in tabs:
        tab_id = tab["id"]
        response = requests.delete(f"{get_route_basket('delete-basket-tab')}{tab_id}",
                                   headers=headers.get_header()
                                   )
        assert response.status_code == 204
        if response.status_code == 204:
            print(f"Tab with id {tab_id} was successfully deleted")
        else:
            print(f"Failed to delete tab with id {tab_id}. Response code: {response.status_code}")
    response = requests.get(get_route_basket('get-basket'),
                            headers=headers.get_header()
                            )
    assert response.status_code == 200
    assert len(response.json()['data']['tabs']) == 0


@pytest.mark.add_product_basket
@pytest.mark.API
def test_add_product_basket():
    body = {
        "vehicleId": 142911,
        "tabType": 2,
        "articleId": 14644872,
        "quantity": 2
    }
    response = requests.post(get_route_basket('post-product'),
                             json=body,
                             headers=headers.get_header()
                             )
    assert response.status_code == 204


@pytest.mark.add_product_basket
@pytest.mark.API
def test_change_qty_basket():
    get_response = requests.get(get_route_basket('get-basket'),
                                headers=headers.get_header()
                                )
    assert get_response.status_code == 200
    product_id = get_response.json()["data"]["tabs"][0]["products"][0]["id"]
    body = {
        "isActive": True,
        "quantity": 10
    }
    response = requests.put(f"{get_route_basket('basket-product-id')}{product_id}",
                            headers=headers.get_header(),
                            json=body
                            )
    assert response.status_code == 200
    get_response = requests.get(get_route_basket('get-basket'),
                                headers=headers.get_header()
                                )
    product_quantity = get_response.json()["data"]["tabs"][0]["products"][0]["quantity"]["value"]
    assert product_quantity == 10


@pytest.mark.add_product_basket
@pytest.mark.API
def test_alternative_basket():
    get_response = requests.get(get_route_basket('get-basket'),
                                headers=headers.get_header()
                                )
    assert get_response.status_code == 200
    product_id = get_response.json()["data"]["tabs"][0]["products"][0]["id"]
    body = {
        "articleId": 7789938
    }
    url = put_basket('basket-alternative-id', product_id)
    put_response = requests.put(url,
                                headers=headers.get_header(),
                                json=body
                                )
    assert put_response.status_code == 200
    get_response2 = requests.get(get_route_basket('get-basket'),
                                 headers=headers.get_header()
                                 )
    get_response_data = get_response2.json()
    product_id_updated = get_response_data["data"]["tabs"][0]["products"][0]["id"]
    assert product_id_updated != product_id



