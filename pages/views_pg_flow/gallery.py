import time

from utils.utilities import Utils
from pages.views_page import Views_pg
from appium.webdriver.common.appiumby import AppiumBy

class Gallery(Views_pg):
    gallery_loc = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Gallery"]')
    photos_button = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="1. Photos"]')
    # photos_loc = (AppiumBy.CLASS_NAME,'android.widget.ImageView')
    photos_loc = (AppiumBy.ID,'io.appium.android.apis:id/gallery')
    imag= (AppiumBy.XPATH,'//android.widget.Gallery[@resource-id="io.appium.android.apis:id/gallery"]/android.widget.ImageView[1]')


    def navigate_to_gallery(self):
        ut = Utils(self.driver)
        self.navigate_to_views()
        ut.clicking_on_ele(self.gallery_loc)

    def select_photos(self):
        ut = Utils(self.driver)
        ut.clicking_on_ele(self.photos_button)

    def swipe_to_images_list(self):
        ut = Utils(self.driver)
        for i in range(5):
            images =ut.elements_list(self.photos_loc)
            if len(images) > 3:
                images[3].click()
                break
            self.driver.swipe(900, 300, 100, 300, 500)
            time.sleep(1)




