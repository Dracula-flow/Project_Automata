from enum import Enum

from pages.base_page import BasePage

from selenium.common.exceptions import NoSuchElementException

class HamburgerOptions(Enum):
    ALL_ITEMS = ("id","inventory_sidebar_link")
    ABOUT = ("id","about_sidebar_link")
    LOGOUT = ("id","logout_sidebar_link")
    RESET_APP_STATE = ("id","reset_sidebar_link")
    SIDE_MENU_CROSS_BTN = ("id","react-burger-cross-btn")

class FilterOptions(Enum):
    NAME_A_TO_Z = ("xpath","//option[@value='az']")
    NAME_Z_TO_A = ("xpath","//option[@value='za']")
    PRICE_LOW_TO_HIGH = ("xpath","//option[@value='lohi']")
    PRICE_HIGH_TO_LOW = ("xpath","//option[@value='hilo']")

class InventoryPage(BasePage):
    TITLE = ("class_name","app_logo")

    HAMBURGER = ("id","react-burger-menu-btn")
    SIDE_MENU = ("class_name","bm-menu")

    CART = ("id","shopping_cart_container")
    CART_BADGE = ("class_name","shopping_cart_badge")

    FILTER = ("class_name", "select_container")
    INVENTORY = ("xpath","//*[@id='inventory_container']")
    
    def get_title(self):
        return self.find(*self.TITLE).text.strip()
    
    def get_hamburger(self):
        return self.find(*self.HAMBURGER)
    
    def open_hamburger(self):
        self.wait_for_clickable(*self.HAMBURGER)
        try:
            self.click(*self.HAMBURGER)
        except Exception:
            pass # If the click fails, it's likely because the hamburger is already open
        
    def is_side_menu_displayed(self):
        try:
            return self.find(*self.SIDE_MENU).is_enabled()
        except NoSuchElementException:
            return False

    def click_hamburger_option(self, option: HamburgerOptions):
        self.open_hamburger()
        self.wait_for_present(*option.value)
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

    def get_filter(self):
        return self.find(*self.FILTER)
    
    def click_filter(self):
        self.click(*self.FILTER)

    def get_filter_option(self, option: FilterOptions):
        self.click_filter()
        return self.find(*option.value)

    def click_filter_option(self, option: FilterOptions):
        self.click(*option.value)