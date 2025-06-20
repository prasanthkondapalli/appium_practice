from pages.views_page import Views_pg
from utils.utilities import Utils
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.



class Datewidges(Views_pg):
    # folder = r'./reports/'
    date_widges_ele = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Date Widgets")')
    dialogue_ele = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="1. Dialog"]')
    change_date_ele = (AppiumBy.XPATH,'//android.widget.Button[@content-desc="change the date"]')
    calender_ele = (AppiumBy.XPATH,'//android.view.View[@resource-id="android:id/month_view"]')
    calender_header_ele = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("android:id/date_picker_header_date")')


    def navigate_to_datewidges(self):
        ut = Utils(self.driver)
        self.navigate_to_views()
        ut.clicking_on_ele(self.date_widges_ele)

    def click_on_dialogue(self):
        ut = Utils(self.driver)
        ut.clicking_on_ele(self.dialogue_ele)











