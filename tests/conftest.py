# Repo file for Pytest's fixtures

import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager as CDM
from webdriver_manager.firefox import GeckoDriverManager as GDM

from config.config import Config

from helpers.auth_helper import AuthHelper


# CLI option to switch browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", 
                     help="Select browser between '--chrome' and '--firefox'")


@pytest.fixture(scope='class')
def driver(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":

        options = ChromeOptions()
        options.add_argument("--disable-extensions")

        service = ChromeService(CDM().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":

        options = FirefoxOptions()
        options.add_argument("--disable-extensions")

        service = FirefoxService(GDM().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture
def auth(driver):
    """
    Fixture to add to tests in order to login with the desired credentials
    """
    return AuthHelper(driver, Config())
