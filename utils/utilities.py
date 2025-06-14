
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class Utils:
    def __init__(self,driver):
        self.driver = driver

    def clicking_on_ele(self,ele):
        ele = self.driver.find_element(AppiumBy.XPATH,ele)
        ele.click()
        return ele
    def took_screenshot(self,path):
        self.driver.save_screenshot(path)

    # def scroll_to_element(self,ele):
    #     ele =self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(newUiSelector().scrollable(true))scrollIntoView(new UiSelector().{ele}')
    #     ele.click()
    #     return ele

    def scroll_to_element(self, ele, max_scrolls=5):
        for _ in range(max_scrolls):
            try:
                element = self.driver.find_element(AppiumBy.XPATH, ele)
                # element.click()
                return element
            except NoSuchElementException:
                self.driver.swipe(500, 500, 500, 500, 1000)
        return None

    def enter_text_in_ele(self,ele,text):
        ele = self.driver.find_element(AppiumBy.XPATH,ele)
        ele.click()
        ele.clear()
        ele.send_keys(text)
        return ele
