import pytest

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup_driver(self, driver,auth):
        self.driver = driver
        self.auth = auth