import pytest
import time

@pytest.mark.parametrize("Username, Password", [('vpatel2894', 'tiku56'), ('vpa6653', '$$$$'),
                                                ('vpatel6653' ,'VrUsHtI94$')])

def test_mynyl(setup):
    setup.get("https://www.mynyl.newyorklife.com/VSCRegWebApp/login?resume=%2Fas%2FMUl6a%2Fresume%2Fas%2Fauthorization.ping&spentity=null")
    setup.find_element_by_xpath("// input[ @ id = 'field-username']").clear()
    setup.find_element_by_xpath("// input[ @ id = 'field-username']").send_keys("Username")
    setup.find_element_by_xpath("// input[ @ id = 'field-password']").clear()
    setup.find_element_by_xpath("// input[ @ id = 'field-password']").send_keys("Password")
    time.sleep(5)





