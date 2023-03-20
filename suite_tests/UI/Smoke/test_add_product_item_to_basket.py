from suite_tests.pom.sign_in_pom import *
from suite_tests.pom.dashboard_pom import *
from suite_tests.pom.catalog_pom import *
from suite_tests.pom.cookie_modal_pom import *

@pytest.mark.usefixtures('setup')
@pytest.mark.SmokeUI
class TestAddProductItems:

    def test_add_product_to_basket(self):
        cookie = CookieModal_POM(self.driver)
        cookie.setup_cookie_modal_true()

        login = SignIn_POM(self.driver)
        login.set_login()
        login.set_password()

        dashboard = Dashboard_POM(self.driver)
        dashboard.create_car_tab_by_reg_number()

        catalog = Catalog_POM(self.driver)
        catalog.go_to_first_catalog_element()
        catalog.go_to_first_catalog_element()
        catalog.add_first_product_item_to_basket()