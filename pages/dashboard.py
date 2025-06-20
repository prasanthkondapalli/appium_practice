from utils.utilities import Utils
from appium.webdriver.common.appiumby import AppiumBy

class Dashboard:
    views_ele = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Views"]')
    web3_ele = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="WebView3"]')

    def __init__(self,driver):
        self.driver = driver

    def navigate_to_views(self):
        ut = Utils(self.driver)
        ut.clicking_on_ele(ele=self.views_ele)

    def navigate_to_web3(self):
        ut = Utils(self.driver)
        ut.clicking_on_ele(ele=self.web3_ele)




