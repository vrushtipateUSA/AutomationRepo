from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(executable_path="/Users/JAY/Desktop/Pycharm Projects/pythonProject/Drivers/chromedriver")
action = ActionChains(driver)
driver.get('https://elgin.edu/')
time.sleep(5)
XPATH1 = "//a[text() = 'Admissions']"
driver.find_element_by_xpath(XPATH1).click()
time.sleep(10)
driver.back()
time.sleep(5)
XPATH2 = "//li[@id='_pay_for_college']/a"
XPATH3 = "//a[text() = 'pay for college']"
driver.find_element_by_xpath(XPATH2).click()
time.sleep(5)
driver.close()