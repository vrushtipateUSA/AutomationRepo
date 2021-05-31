import time

def test_password(setup):
    global driver
    driver = setup
    driver.find_element_by_link_text("Employers").click()
    time.sleep(5)

def test_search(setup):
    driver.find_element_by_xpath("//input[@id = '__BVID__24']").send_keys("Insurance")

def test_back_window(setup):
    driver.back()

def test_cur_emp(setup):
    driver.find_element_by_link_text("Current Employers").click()
    time.sleep(5)

def test_For_emp(setup):
    driver.find_element_by_xpath("//h2[text() = 'For Employees']").click()
    time.sleep(5)

def test_Other_forms(setup):
    driver.find_element_by_xpath("//h2[text() = 'Other Forms']").click()
    time.sleep(5)

def test_AMD_emp(setup):
    driver.find_element_by_link_text("Access Member Documents").click()
    time.sleep(5)

def test_IFD_emp(setup):
    driver.find_element_by_link_text("Individual and Family Plan Documents").click()
    time.sleep(5)

