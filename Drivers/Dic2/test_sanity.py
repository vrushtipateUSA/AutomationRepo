import pytest
import time

@pytest.mark.smoke
def test_Resources(setup):
    setup.find_element_by_link_text("Resources").click()
    setup.find_element_by_link_text("D2L").click()
    global windows
    windows = setup.window_handles
    setup.switch_to.window(windows[1])

@pytest.mark.parametrize("username, password", [('vpatel2894', 'tiku56'), ('vpa6653', '$$$$'), ('vpatel6653' ,'VrUsHtI94$')])
def test_D2l(setup,username,password):

    setup.find_element_by_xpath("//input[@id = 'userName']").clear()
    setup.find_element_by_xpath("//input[@id = 'userName']").send_keys(username)
    setup.find_element_by_xpath("//input[@id = 'password']").clear()
    setup.find_element_by_xpath("//input[@id = 'password']").send_keys(password)
    time.sleep(5)
    #setup.close()
    #setup.switch_to.window(windows[0])



@pytest.mark.sanity
def test_Current_student(setup):
    setup.close()
    setup.switch_to.window(windows[0])
    setup.find_element_by_link_text("Current Students").click()

