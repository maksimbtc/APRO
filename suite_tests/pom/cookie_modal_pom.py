from base.seleniumbase import SeleniumBase

class CookieModal_POM(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cookie_window_class = 'user-consent--6cXc'
        self.cookie_window_button_xpath = "//button[@data-test-id='user-consent-cookies-btn-allow-all']"

    def setup_cookie_modal_true(self):
        self.is_visible('class_name', self.cookie_window_class, 'Cookie modal visibility')
        cookie_window_button = self.is_visible('xpath', self.cookie_window_button_xpath, 'Cookie modal visibility')
        cookie_window_button.click()
        self.is_not_present('class_name', self.cookie_window_class, 'Cookie modal should not be shown')
