from selenium import webdriver
import time
#import pytest
driver = webdriver.Chrome()
driver.get('https://www.bcbstx.com/')
driver.implicitly_wait(10)
driver.maximize_window()
#@pytest.fixture(scope ='function')

driver.find_element_by_xpath("//a[@href = 'https://www.bcbstx.com/employer/index.html']").click()
time.sleep(5)
driver.find_element_by_link_text("Downloadable Forms").click()
time.sleep(5)
#driver.find_element_by_xpath("//a[text() = 'No, thanks']").click()
time.sleep(5)
driver.find_element_by_link_text("Forms for Small Group Products (2-50)").click()
#driver.find_element_by_xpath("//a[text() = 'No, thanks']").click()
time.sleep(5)
#driver.find_element_by_xpath("//a[text() = 'No, thanks']").click()
driver.find_element_by_link_text("Providers").click()
time.sleep(5)
driver.close()
//a[text() = 'Downloadable Forms']