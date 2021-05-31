from selenium import webdriver
import time
import pytest
driver = webdriver.Chrome()
driver.get('https://www.bcbstx.com/')
driver.implicitly_wait(10)
driver.maximize_window()
@pytest.fixture(scope ='function')
def setup():
    print("\n setup function excuted")
    yield
    print("\n Teardown function executed")

def Emp_1():
    driver.find_element_by_xpath("//a[@href = 'https://www.bcbstx.com/employer/index.html']").click()

def setup():
    print("\n setup function executed")
    yield
    print("\n Teardown function executed")
    time.sleep(5)
    driver.find_element_by_link_text("Downloadable Forms").click()





