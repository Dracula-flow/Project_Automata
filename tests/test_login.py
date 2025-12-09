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
        self.login_page.login(self.config.USERNAME_VALID, self.config.PASSKEY)
        assert "inventory.html" in self.login_page.url

    def test_login_wrong_user(self):
        self.login_page.login('mistake', self.config.PASSKEY)

        error_msg = self.login_page.get_error_message()

        expected = "Epic sadface: Username and password do not match any user in this service"

        assert error_msg == expected

    def test_login_wrong_passkey(self):
        self.login_page.login(self.config.USERNAME_VALID, 'fresno')

        error_msg = self.login_page.get_error_message()

        expected = "Epic sadface: Username and password do not match any user in this service"

        assert error_msg == expected
    
    def test_login_locked_out_user(self):
        self.login_page.login(self.config.USERNAME_LOCKED_OUT, self.config.PASSKEY)

        error_msg = self.login_page.get_error_message()
    
        expected = 'Epic sadface: Sorry, this user has been locked out.'

        assert error_msg == expected
    

    
        

