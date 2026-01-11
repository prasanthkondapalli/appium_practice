import time

import pytest
from requests.packages import target
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import Interaction

from pages.views_pg_flow.drag_and_drop import DragandDrop
from utils.utilities import Utils

@pytest.mark.usefixtures("setup_and_tear")
class TestDraagdrop:
    folder = './reports/'

    def test_drag1(self):
        ut = Utils(self.driver)
        dd = DragandDrop(self.driver)
        dd.navigate_to_views()
        dd.click_on_dragndrop()
        action = ActionChains(self.driver)
        dd.drag_and_drop_w3c()
        # target_ele = self.driver.find_elements(dd.target_ele)
        # target_ele2 = self.driver.find_elements(dd.target_ele2)
        # action.move_to_element(dd.target_ele).click_and_hold(dd.target_ele).pause(1).move_to_element(dd.target_ele2).pause(1).release().perform()
        # self.driver.execute_script(
        #     "mobile: dragGesture",
        #     {
        #         "elementId": dd.target_ele,
        #         "endElementId": dd.target_ele2
        #     }
        # )