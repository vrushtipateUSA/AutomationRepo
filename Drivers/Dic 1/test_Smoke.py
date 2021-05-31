import time

def test_members(setup):
    global driver
    driver = setup
    driver.find_element_by_link_text("Members").click()
    time.sleep(5)

def test_username(setup):
    driver.find_element_by_xpath("//input[@id = '__BVID__35']").send_keys("tiku")
    time.sleep(5)

def test_password(setup):
    driver.find_element_by_xpath("//input[@id = '__BVID__37']").send_keys("Shri Krishna")