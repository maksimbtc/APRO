
import time
from selenium.webdriver import Keys
from base.seleniumbase import SeleniumBase
from base.static_info import *

class Catalog_POM(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get('https://test.autodoc.pro/fr/catalog')
        self.first_catalog_element_class = 'card--HGBA'
        self.add_product_button_css = 'td[title="Ajouter"] button'
        self.add_product_notification_class = 'ant-notification-notice-content'


    def go_to_first_catalog_element(self):
        time.sleep(3)
        first_catalog_item = self.is_visible('class_name', self.first_catalog_element_class,
                                             'First catalog element visibility')
        first_catalog_item.click()
        self.is_visible('class_name', self.first_catalog_element_class,
                        'First catalog element visibility')
        return self.driver

    def add_first_product_item_to_basket(self):
        first_catalog_item = self.is_visible('css', self.add_product_button_css,
                                             'First listing product item visibility')
        first_catalog_item.click()
        self.is_visible('class_name', self.add_product_notification_class,
                        'Add product notification element visibility')




