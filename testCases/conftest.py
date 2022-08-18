from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome('/Users/carl/Desktop/Q.A/chromedriver')
#     #driver = webdriver.Chrome(ChromeDriverManager().install())
#     return driver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")