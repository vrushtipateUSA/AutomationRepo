from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/Users/JAY/Desktop/Pycharm Projects/pythonProject/Drivers/chromedriver")
driver.get('http://www.google.com')
time.sleep(2)
driver.get('http://www.mynyl.newyorklife.com')
time.sleep(2)
uname = driver.find_element_by_name("userName")
uname.send_keys('vpatel2894')