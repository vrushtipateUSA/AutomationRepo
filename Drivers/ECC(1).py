from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(executable_path="/Users/JAY/Desktop/Pycharm Projects/pythonProject/Drivers/chromedriver")
action = ActionChains(driver)
driver.get('https://elgin.edu/')
#XPATH3 = "//a[text() = 'Pay for College']"
#XPATH4 = "//a[@class = dropdown-toggle]"
#driver.find_element_by_xpath(XPATH4).click()
#Driver.findElement(By.xpath("//a[text()='App Configuration']")).click();
#selenium.FindElement(By.XPath("xpath=//a[contains(@href,'listDetails.do')")).Click();
#time.sleep(5)
#driver.findElement(By.xpath("(.//[@href='/docs/configuration'])")).click();
#driver.find_element_by_partial_link_text("text").click()
#IWebElement username = Driver.FindElement(By.XPath("//input[contains(@id, 'UserName')]" ));
#username = driver.find_element_by_name('username')
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
driver.quit()
XPATH6 = "/a[@href = "/admissions/"]//following::li[@id = '_pay_for_college']/a[text()='Pay for College']"
#syntax : //reftag[@attribute='value']//following::tar-tag
# example : //input[@id='travlastname']//following::p[@id='addmorepax_field']
driver.find_element_by_xpath(XPATH6).click()
