
from pages.base_page import BasePage

# TODO 1: Define which tests could be performed on the main page
# TODO 2: Define what helper methods could be needed in the main page for the tests

class InventoryPage(BasePage):
    TITLE = ("class_name","app_logo")

    HAMBURGER = ("id","react-burger-menu-btn")

    ALL_ITEMS_LINK = ("id","inventory_sidebar_link")
    ABOUT_LINK = ("id","about_sidebar_link")
    LOGOUT_LINK = ("id","logout_sidebar_link")
    RESET_APP_STATE_LINK = ("id","reset_sidebar_link")

    CART = ("id","shopping_cart_container")
    FILTER = ("class_name", "select_container")
    INVENTORY = ("xpath","//*[@id='inventory_container']")
    
    def get_title(self):
        return self.find(*self.TITLE).text.strip()
    
    def get_hamburger(self):
        return self.find(*self.HAMBURGER)
    
    def open_hamburger(self):
        self.click(*self.HAMBURGER)
    
    def go_to_cart(self):
        self.click(*self.CART)

    
    
