import pytest

from tests.base_test import BaseTest
from pages.login_page import LoginPage
from config.config import Config

class TestLogin(BaseTest):
    config = Config()

    @pytest.fixture(autouse=True)
    def setup(self):
        self.login_page = LoginPage(self.driver)
        self.driver.get(self.config.BASE_URL)

    def test_login_success(self):
        self.login_page.login(self.config.USERNAME_VALID, self.config.PASSKEY)
        assert "inventory.html" in self.login_page.get_url

    def test_login_wrong_user(self):
        self.login_page.login('mistake', self.config.PASSKEY)
        error_button = self.login_page.wait_for_present('class_name', 'error-button')

        assert error_button.is_displayed()
        

