from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(executable_path="/Users/JAY/Desktop/Pycharm Projects/pythonProject/Drivers/chromedriver")
action = ActionChains(driver)
driver.get('https://elgin.edu/')
time.sleep(5)
driver.find_element_by_partial_link_text("Current Students").click()
time.sleep(5)
XPATH1 = "//a[@title='accessECC Portal']"
driver.find_element_by_xpath(XPATH1).click()
time.sleep(5)
XPATH2 = "//input[@id = 'userNameInput']"
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath(XPATH2).send_keys("vpatel6653")
time.sleep(5)
#XPATH3 = "//div[@id = 'passwordArea']"
XPATH4 = "//input[@name = 'Password']"
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath(XPATH4).send_keys("VrUsHtI94$")
driver.back()
driver.back()
XPATH5 = "//div[@id = 'kmsiArea']"
driver.find_element_by_xpath(XPATH5).click()
driver.get('https://elgin.edu/')
time.sleep(5)
XPATH6 = "//a[text() = 'Resources']"
driver.find_element_by_xpath(XPATH6).click()






