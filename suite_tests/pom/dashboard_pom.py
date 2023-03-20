from selenium.webdriver import Keys

from base.seleniumbase import SeleniumBase
from base.static_info import *
from suite_tests.UI.config.api_hook import *

class Dashboard_POM(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get('https://test.autodoc.pro/fr/dashboard')
        self.catalog_page_menu = 'https://test.autodoc.pro/fr/catalog'
        self.reg_number_input_id = 'carRegNumber'
        self.CAR_TAB_TEXT = "BMW 3 Berline (E46)"

    def go_to_catalog(self):
        self.driver.get(self.catalog_page_menu)
        self.is_visible('class_name', 'text--fno_', 'Catalog visibility')
        return self.driver

    def create_car_tab_by_reg_number(self):
        token = auth()
        test_delete_all_vehicle_tabs(token)

        reg_number_field = self.is_visible('id', self.reg_number_input_id, 'Create car tab form visibility')
        reg_number_field.send_keys(REG_NUMBER)
        reg_number_field.send_keys(Keys.ENTER)
        return self.driver