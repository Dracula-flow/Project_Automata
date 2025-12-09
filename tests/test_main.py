import pytest

from tests.base_test import BaseTest
from pages.main_page import MainPage

class TestMain(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.login_page = MainPage(self.driver)
        self.driver.get(self.config.BASE_URL)
