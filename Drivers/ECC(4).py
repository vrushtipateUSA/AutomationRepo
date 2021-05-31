from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#driver = webdriver.Chrome(executable_path="/Users/JAY/Downloads/chromedriver")
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(10)
driver.get('https://www.niche.com/colleges/search/best-colleges/')



