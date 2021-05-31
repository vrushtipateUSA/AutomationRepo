import pytest
import time

@pytest.mark.usefixtures("class_setup")
class TestMyECC():

    @pytest.mark.smoke
    @pytest.mark.usefixtures("test_setup")
    def test_pay_for_college(self):
        self.driver.find_element_by_xpath("(//a[text() = 'Pay for College'])[2]").click()
        time.sleep(5)

    @pytest.mark.sanity
    @pytest.mark.usefixture("test_setup")
    def test_tuition_fees(self):
        self.driver.find_element_by_link_text("Tuition & Fees").click()
        time.sleep(5)