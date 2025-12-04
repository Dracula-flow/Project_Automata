from config.config import Config

# magari includiamo page factory? Non suona male
class BaseTest:
    driver = None
    config = Config()

    def click(self, element):
        pass
