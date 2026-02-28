import pytest

from tests.base_test import BaseTest
from pages.inventory_page import MainPage
from config.config import Config

class TestInventory(BaseTest):
    config = Config()

    @pytest.fixture(autouse=True)
    def setup(self):
        self.login_page = MainPage(self.driver)
        self.driver.get(self.config.BASE_URL)
        self.auth.login(self.config.USERNAME_VALID, self.config.PASSKEY)

    def test_title(self):
        
