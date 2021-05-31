import pytest
from selenium import webdriver

driver = None

def start_browser():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://elgin.edu/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope='session')
def setup():
    driver = start_browser()
    return driver

@pytest.fixture(scope='class')
def class_setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://elgin.edu/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope = 'function')
def test_setup():
    print("\n Test execution started")
    yield
    print("\n Test execution finished")
