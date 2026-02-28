import pytest

from tests.base_test import BaseTest
from pages.inventory_page import InventoryPage
from config.config import Config

class TestInventory(BaseTest):
    config = Config()

    @pytest.fixture(autouse=True)
    def setup(self,auth):
        self.inventory_page = InventoryPage(self.driver)
        self.driver.get(self.config.BASE_URL)
        auth.login(self.config.USERNAME_VALID, self.config.PASSKEY)

    def test_title(self):
        title = self.inventory_page.get_title()

        expected = "Swag Labs"

        assert title == expected
        
