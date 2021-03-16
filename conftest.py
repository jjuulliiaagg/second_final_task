import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# @pytest.fixture()
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
    browser.get('http://127.0.0.1:8000/')
    print('ok')
    # browser.maximize_window()
    # browser.implicitly_wait(5)
    # yield browser
    browser.quit()



if __name__ == '__main__':
    browser()