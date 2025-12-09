from pages.login_page import LoginPage

class AuthHelper:
    """
    A helper class for the website login.

    Combined with a pytest fixture in conftest.py, it allows the tester to choose the credentials to use for the login in the test files.
    """
    def __init__(self, config, driver):
        self.config = config
        self.driver = driver
        
    def login(self, username, password):
        login_page = LoginPage(self.driver)
        self.driver.get(self.config.BASE_URL)
        login_page.login(username, password)

        return self.driver

