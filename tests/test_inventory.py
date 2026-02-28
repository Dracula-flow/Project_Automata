import pytest

from tests.base_test import BaseTest
from pages.inventory_page import InventoryPage, HamburgerOptions
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
        
    def test_cart(self):
        self.inventory_page.go_to_cart()

        assert "cart.html" in self.inventory_page.url

    def test_open_hamburger(self):
        self.inventory_page.open_hamburger()

        link = self.inventory_page.get_hamburger_option(HamburgerOptions.ALL_ITEMS)
        assert link

    def test_hamburger_all_items(self):
        self.inventory_page.go_to_cart() # to make sure we are not on the inventory page already

        self.inventory_page.click_hamburger_option(HamburgerOptions.ALL_ITEMS)

        assert "inventory.html" in self.inventory_page.url

    def test_hamburger_about(self):
        self.inventory_page.click_hamburger_option(HamburgerOptions.ABOUT)

        assert "saucelabs.com" in self.inventory_page.url

    def test_hamburger_logout(self):
        self.inventory_page.click_hamburger_option(HamburgerOptions.LOGOUT)

        assert self.inventory_page.url == self.config.BASE_URL

    def test_hamburger_reset_app_state(self):
        self.inventory_page.add_backpack_to_cart()

        assert self.inventory_page.get_cart_badge_count() > 0 # to make sure that the badge is visible

        self.inventory_page.click_hamburger_option(HamburgerOptions.RESET_APP_STATE)
        
        assert self.inventory_page.get_cart_badge_count() == 0