
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException



class Utils:
    def __init__(self,driver):
        self.driver = driver

    def long_press_ele(self,ele):
        element = self.driver.find_element(*ele).longClick()
        return element

    def elements_list(self,ele):
        try:
            e = self.driver.find_elements(*ele)
        except Exception as e:
            print('elements__:: ',e)
        return e

    def ele_drag_drop(self,ele1,ele2):
        e1 = self.driver.find_element(*ele1)
        e2 = self.driver.find_element(*ele2)
        self.driver.drag_and_drop(e1,e2)

    def clicking_on_ele(self,ele):
        e = self.driver.find_element(*ele)
        e.click()
        return e
    def took_screenshot(self,path):
        self.driver.save_screenshot(path)

    def return_ele(self,ele):
        e=None
        try:
            e = self.driver.find_element(*ele)
        except Exception as el:
            print(f'Element not found {ele} with error {el}')
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
