import time

from selenium.webdriver.common.by import By

from base.seleniumbase import SeleniumBase
from base.static_info import *
from selenium.webdriver.common.keys import Keys

class SignIn_POM(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get('https://test.autodoc.pro/fr/signin')

        self.email_input_id = 'login'
        self.password_input_id = 'password'
        self.TITLE_PAGE = 'title'
        self.agree_cookie_modal_button_class = 'ant-btn ant-btn-primary ant-btn-block btn--9PFw user-consent-button--81J_'

    def set_login(self):
        email_field = self.is_visible('id', self.email_input_id, 'Email field visibility')
        email_field.send_keys(LOGIN_CRED)
        return self.driver

    def set_password(self):
        password_field = self.is_visible('id', self.password_input_id, 'Password field visibility')
        password_field.send_keys(PASSWORD_CRED)
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element(By.TAG_NAME, self.TITLE_PAGE)
        return self.driver


