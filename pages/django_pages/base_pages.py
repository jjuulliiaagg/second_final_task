
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = 'http://127.0.0.1:8000/'

    def open_base_page(self):
        self.driver.get(self.base_page)
