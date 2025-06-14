import time

import pytest
from pages.dashboard import Dashboard
from utils.utilities import Utils
from pages.views_page import Views_pg

@pytest.mark.usefixtures("setup_and_tear")
class Testdashboard:

    def test_d(self):
        db = Dashboard(self)
        ut = Utils(self.driver)
        ut.clicking_on_ele(ele=db.views_ele)
        time.sleep(3)

        ut.took_screenshot("./reports/sc.png")
        print("test click")
        pass

    def test_web3(self):
        db = Dashboard(self.driver)
        ut = Utils(self.driver)
        db.navigate_to_views()
        ut.scroll_to_element(ele=db.web3_ele)
        # db.navigate_to_web3()
        ut.took_screenshot('./reports/web3.png')
        print("Test_pass")

    def test_3(self):
        db = Views_pg(self.driver)
        ut = Utils(self.driver)
        db.navigate_to_controls()
        ut.clicking_on_ele(db.light_theme_ele)
        ut.took_screenshot(path="./reports/test3.png")
        print("test_passed")

