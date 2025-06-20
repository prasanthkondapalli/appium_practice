from utils.utilities import Utils
from pages.views_pg_flow.date_widges import Datewidges
import pytest

@pytest.mark.usefixtures("setup_and_tear")
class TestDateWidges:
    folder = './reports/'

    def test_date(self):
        ut = Utils(self.driver)
        dw = Datewidges(self.driver)

        dw.navigate_to_datewidges()
        dw.click_on_dialogue()
        ut.clicking_on_ele(dw.change_date_ele)
        ele = ut.return_ele(dw.calender_header_ele)
        print(ele.text)
        ut.took_screenshot(self.folder+'date.png')


