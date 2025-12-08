from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = ("id", "user-name")
    USERNAME_PASSWORD = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")

    def login(self, username, password):
        self.type(username, *self.USERNAME_INPUT)
        self.type(password, *self.USERNAME_PASSWORD)
        self.click(*self.LOGIN_BUTTON)
