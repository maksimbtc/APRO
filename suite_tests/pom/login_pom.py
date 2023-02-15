from base.seleniumbase import SeleniumBase


class Login_POM(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__coolie_modal_text: str = '#__next>div>section>div>div>div.ant-row.user-consent-content--UycV>div>h3'
        self.COOKIE_TITLE_TEXT = 'This web site uses cookies'

    def get_cookie_modal_text(self) -> str:
        title_cookie_text = self.is_visible('css', self.__coolie_modal_text, 'Text cookie visibility').text
        return "".join(title_cookie_text)



