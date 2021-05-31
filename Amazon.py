from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(executable_path="/Users/JAY/Desktop/Pycharm Projects/pythonProject/Drivers/chromedriver")
action = ActionChains(driver)
driver.get('http://www.google.com')
time.sleep(5)
driver.get('http://www.amazon.com')
time.sleep(2)
Menu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[1]')
action.move_to_element(Menu).perform()
Account = driver.find_element_by_xpath('//*[@id="nav-al-your-account"]/a[1]/span')
action.move_to_element(Account).perform()
AccountPage = driver.find_element_by_xpath('//*[@id="nav-al-your-account"]/a[1]/span')
AccountPage.click()
driver.find_element_by_xpath('//*[@id="a-page"]/div[2]/div/div[2]/div[1]/a/div/div/div/div[2]/h2').click()
Sign = driver.find_element_by_xpath('//*[@id="ap_email"]')
Sign.send_keys('vrushti.jigar67@gmail.com')
ele = driver.find_element_by_id('continue')
ele.click()
pwd = driver.find_element_by_name('password')
pwd.click()
pwd.send_keys('VrUsHtI94$')
sub = driver.find_element_by_id('signInSubmit')
sub.click()










