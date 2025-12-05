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
        self.login_page.login(self.config.USERNAME, self.config.PASSKEY)
        assert "Swag Labs" in self.login_page.get_title()

