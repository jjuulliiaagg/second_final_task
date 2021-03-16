import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome('http://localhost:8000/', options=chrome_options)
    # browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()



