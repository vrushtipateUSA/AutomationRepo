import pytest
from selenium import webdriver

driver = None

def start_browser():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.southcarolinablues.com/web/public/brands/sc/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope = 'session')
def setup():
    driver = start_browser()
    return driver

