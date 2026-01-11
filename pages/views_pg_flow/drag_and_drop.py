from selenium.webdriver.common.by import By

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from pages.views_page import Views_pg
from utils.utilities import Utils
from appium.webdriver.common.appiumby import AppiumBy


class DragandDrop(Views_pg):

    drag_and_drop_ele = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Drag and Drop")')

    target_ele = (By.XPATH,'//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_1"]')
    # target_ele = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("io.appium.android.apis:id/drag_dot_1")')
    # target_ele2 = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("io.appium.android.apis:id/drag_dot_2")')
    target_ele2 = (By.XPATH,'//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_2"]')
    # target_ele = (AppiumBy.ID,'io.appium.android.apis:id/drag_dot_1')


    target2_ele = (AppiumBy.ID,'io.appium.android.apis:id/drag_dot_2')
    ele_1 = ()

    def click_on_dragndrop(self):
        ut = Utils(self.driver)
        ut.clicking_on_ele(self.drag_and_drop_ele)

    def do_drag_drop(self):
        self.driver.execute_script("mobile: dragGesture",{"elementId":self.target_ele,"endElementId":self.target2_ele})


    def drag_and_drop_w3c(self):
        # Locate elements using Appium locators
        source = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("io.appium.android.apis:id/drag_dot_1")'
        )
        print(source)
        target = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("io.appium.android.apis:id/drag_dot_2")'
        )
        print(target)

        # Get element center coordinates
        # start_x = source.location['x'] + source.size['width'] // 2
        # start_y = source.location['y'] + source.size['height'] // 2
        # end_x = target.location['x'] + target.size['width'] // 2
        # end_y = target.location['y'] + target.size['height'] // 2

        # Create a touch pointer
        # touch_input = PointerInput(PointerInput.TOUCH, "finger")
        #
        # # Build the action sequence
        # actions = ActionBuilder(self.driver)
        # actions.add_action(touch_input)
        #
        # # Drag-and-drop sequence
        # touch_input.create_pointer_move(duration=0, x=start_x, y=start_y)  # move finger to start
        # touch_input.create_pointer_down()                                   # touch down
        # touch_input.create_pause(0.5)                                       # optional pause
        # touch_input.create_pointer_move(duration=1000, x=end_x, y=end_y)    # move to target
        # touch_input.create_pointer_up()                                     # lift finger
        #
        # # Perform the actions
        # actions.perform()

        # def drag_and_drop_w3c(self):
            # Find elements
        # source = self.driver.find_element(source)
        # target = self.driver.find_element(target)

        # Get center coordinates
        start_x = source.location['x'] + source.size['width'] // 2
        start_y = source.location['y'] + source.size['height'] // 2
        end_x = target.location['x'] + target.size['width'] // 2
        end_y = target.location['y'] + target.size['height'] // 2

        # Create touch pointer
        finger = PointerInput("touch", "finger")  # <-- FIX HERE
        actions = ActionBuilder(self.driver)
        actions.add_pointer_input('touch','finger')

        # Build drag-and-drop sequence
        finger.create_pointer_move(0, start_x, start_y)
        finger.create_pointer_down()
        finger.create_pause(0.5)
        finger.create_pointer_move(1000, end_x, end_y)
        finger.create_pointer_up(button=0)
        actions.perform()


