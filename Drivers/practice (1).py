from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('https://www.bcbstx.com/')
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)
#driver.find_element_by_link_text("//a[@href = 'https://www.bcbstx.com/employer/index.html']").click()
#driver.find_element_by_partial_link_text("//a[@href = 'https://www.bcbstx.com/employer/index.html']").click()
#Var1 = driver.find_element_by_link_text("Employers")
#Var1.click()
driver.find_element_by_xpath("//a[@href = 'https://www.bcbstx.com/employer/index.html']").click()
time.sleep(5)
#driver.find_element_by_xpath("//a[@href =' https://www.bcbstx.com/employer/resources/index.html]").click()
driver.find_element_by_link_text("Employer Resources").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@id = 'txtop']").click()
time.sleep(5)
#driver.find_element_by_xpath("//a[@text = 'View all']").click()
driver.find_element_by_link_text("View all").click()
driver.find_element_by_xpath("//a[text() = 'No, thanks']").click()
time.sleep(5)
driver.find_element_by_link_text("Online Bill Payment").click()
time.sleep(5)
driver.back()
driver.back()
driver.back()
driver.find_element_by_name('USER').send_keys('tiku')
driver.save_screenshot('BCBS.png')











