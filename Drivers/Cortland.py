from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/Users/JAY/Desktop/Pycharm Projects/pythonProject/Drivers/chromedriver")
driver.get('https://cortland.com/apartments/cortland-allen-station/')
time.sleep(2)
#XPATH1 = '//*[@id="headerContent"]/div[1]/div[3]/a'
#driver.find_element_by_xpath(XPATH1).click()
#driver.quit()
#XPATH2 = '/button[@class = 'header__toolbar-link header__toolbar-link--single']//following-sibling::a[@class = 'header__toolbar-link--extra header__toolbar-link']'
XPATH3 = "//button[text() = 'Contact Us']//following::a[text() = 'Residents' and @data-event-label='Utility Bar']"
driver.find_element_by_xpath(XPATH3).click()
XPATH4 = '//span[@class="hamburger__wrapper"]'
driver.find_element_by_xpath(XPATH4).click()
XPATH5 = "//a[@data-event-label = 'Home']//following-sibling::a[text() = 'Floor Plans']"
driver.find_element_by_xpath(XPATH5).click()
