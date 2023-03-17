import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from suite_tests.UI.config.api_hook import *


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('headless')  # use headless if you don't need a browser UI
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture(scope='function')  # scope='function' run before each test. session - scope for all session of browser (after all tests)
def setup(request, get_webdriver):
    before_api_hook()
    driver = get_webdriver
    url = 'https://test.autodoc.pro/en/signin'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)  # run is from class or no
    yield driver
    driver.quit()

def before_api_hook():
    token = auth()
    add_bank_details(token)
    add_working_hours(token)

