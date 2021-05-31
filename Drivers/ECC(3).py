from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(executable_path="/Users/JAY/Desktop/Pycharm Projects/pythonProject/Drivers/chromedriver")
action = ActionChains(driver)
driver.get('https://elgin.edu/')
driver.find_element_by_xpath('//*[@id="_pay_for_college"]/a').click()
time.sleep(5)
driver.back()
XPATH5= "//a[@data-target = '.utility-nav']"
driver.find_element_by_xpath(XPATH5).click()
time.sleep(5)
driver.find_element_by_partial_link_text("D2L").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.find_element_by_xpath("//input[@name = 'userName']").send_keys('vpatel6653')
time.sleep(5)
driver.find_element_by_xpath("//input[@type = 'password']").send_keys('VrUsHtI94$')
time.sleep(5)
driver.get('https://elgin.edu/')
time.sleep(5)
XPATH6 = "//a[@href ='/admissions/']//following::li[@id='_pay_for_college']"
driver.find_element_by_xpath(XPATH6).click()
time.sleep(5)
XPATH7 = "//a[@href ='/academics/']//following::li[@id='_life_at_ecc']"
driver.find_element_by_xpath(XPATH7).click()
