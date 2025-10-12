import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from pages.views_pg_flow.drag_and_drop import DragandDrop
from utils.utilities import Utils

@pytest.mark.usefixtures("setup_and_tear")
class TestDraagdrop:
    folder = './reports/'

    def test_drag1(self):
        action = ActionChains(self.driver)
        ut = Utils(self.driver)
        dd = DragandDrop(self.driver)
        dd.navigate_to_views()
        dd.click_on_dragndrop()
        dd.do_drag_drop()
        # ut.clicking_on_ele(dd.target_ele)
        # # action.click_and_hold(dd.target_ele)
        # time.sleep(2)
        # action.drag_and_drop_by_offset(dd.target2_ele,653,536)
        # # dd.click_on_dragndrop()
        # ut.long_press_ele(dd.target_ele)
        # ut.ele_drag_drop(dd.target_ele,dd.target2_ele)
        # ut.took_screenshot(path=f'{self.folder}drag1.png')
