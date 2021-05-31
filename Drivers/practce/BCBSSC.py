from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.southcarolinablues.com/web/public/brands/sc/employers/")
driver.implicitly_wait(10)
driver.maximize_window()
Emp1 = driver.find_element_by_link_text("Employers").click()
time.sleep(5)
CurEmp = driver.find_element_by_link_text("Current Employers").click()
time.sleep(5)
ForEmp = driver.find_element_by_xpath("//h2[text() = 'For Employees']").click()
time.sleep(5)
Otherfor = driver.find_element_by_xpath("//h2[text() = 'Other Forms']").click()
time.sleep(5)
AMD = driver.find_element_by_link_text("Access Member Documents").click()
time.sleep(5)
IFD = driver.find_element_by_link_text("Individual and Family Plan Documents").click()
time.sleep(5)
IFD1 = driver.find_element_by_link_text("2021 BlueEssentials Policy and Outline of Coverage").click()





