import pytest
from suite_tests.pom.login_pom import Login_POM


@pytest.mark.usefixtures('setup')
class TestLogInForm:

    def test_LogInForm(self):
        login = Login_POM(self.driver)
        actual_text = login.get_cookie_modal_text()
        expected_text = login.COOKIE_TITLE_TEXT
        assert expected_text == actual_text, 'Validating title text on cookie modal'
