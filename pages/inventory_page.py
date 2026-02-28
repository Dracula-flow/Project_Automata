from enum import Enum

from pages.base_page import BasePage

# TODO 1: Define which tests could be performed on the main page
# TODO 2: Define what helper methods could be needed in the main page for the tests

class HamburgerOptions(Enum):
    ALL_ITEMS = ("id","inventory_sidebar_link")
    ABOUT = ("id","about_sidebar_link")
    LOGOUT = ("id","logout_sidebar_link")
    RESET_APP_STATE = ("id","reset_sidebar_link")

class InventoryPage(BasePage):
    TITLE = ("class_name","app_logo")

    HAMBURGER = ("id","react-burger-menu-btn")

    CART = ("id","shopping_cart_container")
    CART_BADGE = ("class_name","shopping_cart_badge")

    FILTER = ("class_name", "select_container")
    INVENTORY = ("xpath","//*[@id='inventory_container']")
    
    def get_title(self):
        return self.find(*self.TITLE).text.strip()
    
    def get_hamburger(self):
        return self.find(*self.HAMBURGER)
    
    def open_hamburger(self):
        self.wait_for_visible(*self.HAMBURGER)
        self.click(*self.HAMBURGER)

    def click_hamburger_option(self, option: HamburgerOptions):
        self.open_hamburger()
        self.click(*option.value)
        
    def get_hamburger_option(self, option: HamburgerOptions):
        self.open_hamburger()
        return self.find(*option.value)
            
    def go_to_cart(self):
        self.click(*self.CART)

    def get_cart_badge_count(self):
        try:
          return int(self.find(*self.CART_BADGE).text)
        except:
            return 0
    
    def add_backpack_to_cart(self):
        self.click("id", "add-to-cart-sauce-labs-backpack")
