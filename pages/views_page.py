from appium.webdriver.common.appiumby import AppiumBy

from pages.dashboard import Dashboard
from utils.utilities import Utils

class Views_pg(Dashboard):
    folder = './reports/'
    controls_ele = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Controls"]')
    light_theme_ele = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="1. Light Theme"]')
    check_box1_ele = (AppiumBy.XPATH,'//android.widget.CheckBox[@content-desc="Checkbox 1"]')
    check_box2_ele = (AppiumBy.XPATH,'//android.widget.CheckBox[@content-desc="Checkbox 2"]')
    radio_button1_ele = (AppiumBy.XPATH,'//android.widget.RadioButton[@content-desc="RadioButton 1"]')
    radio_button2_ele =(AppiumBy.XPATH,'//android.widget.RadioButton[@content-desc="RadioButton 2"]')
    hint_text_ele = (AppiumBy.XPATH,'//android.widget.EditText[@resource-id="io.appium.android.apis:id/edit"]')
    def click_on_constrols(self):
        ut = Utils(self.driver)
        ut.clicking_on_ele(self.controls_ele)

    def navigate_to_controls(self):
        self.navigate_to_views()
        self.click_on_constrols()

    def navigate_to_lighttheme(self):
        self.navigate_to_controls()
        ut = Utils(self.driver)
        ut.clicking_on_ele(self.light_theme_ele)
