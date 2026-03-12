
from pages.views_page import Views_pg
from utils.utilities import Utils
from appium.webdriver.common.appiumby import AppiumBy


class DragandDrop(Views_pg):

    drag_and_drop_ele = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Drag and Drop")')

    target_ele = (AppiumBy.ID, "io.appium.android.apis:id/drag_dot_1")
    target_ele2 = (AppiumBy.ID, "io.appium.android.apis:id/drag_dot_2")

    def click_on_dragndrop(self):
        ut = Utils(self.driver)
        ut.clicking_on_ele(self.drag_and_drop_ele)

    def do_drag_drop(self):
        self.driver.execute_script("mobile: dragGesture",{"elementId":self.target_ele,"endElementId":self.target2_ele})


    def drag_and_drop_mobile(self):
        ut = Utils(self.driver)
        source = ut.return_ele(self.target_ele)
        target = ut.return_ele(self.target_ele2)
        start_x = source.location['x'] + source.size['width'] // 2
        start_y = source.location['y'] + source.size['height'] // 2
        end_x = target.location['x'] + target.size['width'] // 2
        end_y = target.location['y'] + target.size['height'] // 2

        self.driver.execute_script(
            "mobile: dragGesture",
            {
                "startX": start_x,
                "startY": start_y,
                "endX": end_x,
                "endY": end_y,
                "speed": 2500
            }
        )



