
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class Utils:
    def __init__(self,driver):
        self.driver = driver

    def clicking_on_ele(self,ele):
        e = self.driver.find_element(*ele)
        e.click()
        return e
    def took_screenshot(self,path):
        self.driver.save_screenshot(path)

    def return_ele(self,ele):
        e = self.driver.find_element(*ele)
        return e

    def scroll_to_element(self, ele, max_scrolls=5):
        for _ in range(max_scrolls):
            try:
                element = self.driver.find_element(*ele)
                # element.click()
                return element
            except NoSuchElementException:
                self.driver.swipe(500, 500, 500, 500, 1000)
            except Exception as e:
                print("No element found")
        return None

    def enter_text_in_ele(self,ele,text):
        ele = self.driver.find_element(*ele)
        ele.click()
        ele.clear()
        ele.send_keys(text)
        return ele
