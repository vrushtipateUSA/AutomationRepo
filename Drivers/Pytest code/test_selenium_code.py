from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome()
#driver.get('https://www.bcbstx.com/')
#driver.implicitly_wait(10)
#driver.maximize_window()
driver = None
@pytest.fixture(scope ='module')
def setup():
    global driver
    print("\n setup function excuted")
    driver = webdriver.Chrome()
    driver.get('https://www.bcbstx.com/')
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield
    driver.close()
    print("\n Teardown function executed")

def test_employers(setup):
    driver.find_element_by_xpath("//a[@href = 'https://www.bcbstx.com/employer/index.html']").click()
    time.sleep(5)

def test_employer_resources(setup):
    driver.find_element_by_link_text('Employer Resources').click()
    driver.find_element_by_xpath("//div[@id = 'txtop']").click()

#def test_employer_viewall():
 #   driver.find_element_by_link_text('View all').click()
   # driver.find_element_by_xpath("//a[text() = 'No, thanks']").click()



