from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import Logger
from utils.decorators import log_action

class BasePage:
    """
    Foundation for Page objects, home of helper methods.

    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = Logger(self.__class__.__name__)

    @log_action(level="debug")
    def find(self, by, value=None):
        """
        Wrapper for driver.find_element.
        Supports both:
            - Individual strings: self.find("id", "textblock")
            - Classic tuple: self.find((By.ID, "textblock"))
        """

        by,value = self._normalize_locator(by,value)
        return self.driver.find_element(by, value)
    
    @log_action(level="debug")
    def finds(self, by, value=None):
        """
        Wrapper for driver.find_elements with same behavior as find():
        Supports both:
            - Individual strings: self.find("id", "textblock")
            - Classic tuple: self.find((By.ID, "textblock"))
        """

        by,value = self._normalize_locator(by,value)
        return self.driver.find_elements(by, value)

    @log_action(level="info")
    def wait_for_present(self, by, value=None, condition = EC.presence_of_element_located):
        """
        Wrapper for driver.wait.until.EC.presence_of_element_located.
        Supports both:
            - Individual strings: self.find("id", "textblock")
            - Classic tuple: self.find((By.ID, "textblock"))
         
        """

        by,value = self._normalize_locator(by,value)
        return self.wait.until(condition ((by,value)) )
    
    @log_action(level="info")
    def wait_for_clickable(self, by, value=None, condition = EC.element_to_be_clickable):
        """
        Wrapper for driver.wait.until.EC.element_to_be_clickable.
        Supports both:
            - Individual strings: self.find("id", "textblock")
            - Classic tuple: self.find((By.ID, "textblock"))
         
        """

        by,value = self._normalize_locator(by,value)
        return self.wait.until(condition ((by,value)) )
    
    @log_action(level="info")
    def wait_for_disappear(self, by, value=None, condition = EC.invisibility_of_element_located):
        """
        Wrapper for driver.wait.until.EC.invisibility_of_element_located.
        Supports both:
            - Individual strings: self.find("id", "textblock")
            - Classic tuple: self.find((By.ID, "textblock"))
         
        """

        by,value = self._normalize_locator(by,value)
        return self.wait.until(condition ((by,value)) )
    
    @log_action(level="info")
    def wait_for_visible(self, by, value=None, condition = EC.visibility_of_element_located):
        """
        Wrapper for driver.wait.until.EC.visibility_of_element_located.
        Supports both:
            - Individual strings: self.wait_for_visible("id", "textblock")
            - Classic tuple: self.find((By.ID, "textblock"))
         
        """

        by,value = self._normalize_locator(by,value)
        return self.wait.until(condition ((by,value)) )
    
    @log_action(level="info")
    def click(self, by, value=None):
        el = self.wait_for_clickable(by, value)
        el.click()
        return el # for chaining
    
    @log_action(level="info")
    def type(self, text, by, value=None):
        el = self.find(by, value)
        el.clear()
        el.send_keys(text)
        return el
    
    @log_action(level="debug")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    @log_action(level="info")
    def go_to(self, url):
        self.driver.get(url)

    @log_action(level="info")
    def refresh(self):
        self.driver.refresh()

    def _normalize_locator(self, by, value=None):
        """
        Helper method. Normalizes strings or tuple locators into (By, value)
        
        """
        if value is None:
            # assumes that user passed a Tuple
            by, value = by

        if isinstance(by, str):
            try:
                by= getattr(By, by.upper())
            except AttributeError:
                raise ValueError(f"Invalid locator strategy: '{by}';")
        
        return by,value

    @property
    def title(self):
        """
        Returns title of the page.
        """
        return self.driver.title
    
    @property
    def url(self):
        """
        Returns current URL.
        """
        return self.driver.current_url
    

