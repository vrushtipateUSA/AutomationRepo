from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/Users/JAY/Desktop/Pycharm Projects/pythonProject/Drivers/chromedriver")
driver.get('http://www.google.com')
driver.get('http://www.elgin.edu')
time.sleep(5)
driver.find_element_by_link_text('Resources').click()
time.sleep(5)
driver.find_element_by_link_text('accessECC').click()
driver.find_elements_by_id("userNameInput").send_keys('username')





