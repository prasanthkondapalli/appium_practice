from selenium.webdriver.common.by import By

from pages.views_page import Views_pg
from utils.utilities import Utils
from appium.webdriver.common.appiumby import AppiumBy


class DragandDrop(Views_pg):

    drag_and_drop_ele = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Drag and Drop")')
    # target_ele = (By.XPATH,'//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_1"]')
    target_ele = (AppiumBy.ID,'io.appium.android.apis:id/drag_dot_1')
    target2_ele = (AppiumBy.ID,'io.appium.android.apis:id/drag_dot_2')


    def click_on_dragndrop(self):
        ut = Utils(self.driver)
        ut.clicking_on_ele(self.drag_and_drop_ele)

    def do_drag_drop(self):
        self.driver.execute_script("mobile: dragGesture",{"elementId":self.target_ele,"endElementId":self.target2_ele})

