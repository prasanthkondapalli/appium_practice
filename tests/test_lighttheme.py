import pytest, time
from utils.utilities import Utils
from pages.views_page import Views_pg

@pytest.mark.usefixtures("setup_and_tear")
class Testlighttheme:
    folder = r'./reports/'

    # @pytest.mark.parametrize("txt",["txt1",'test 123',12334])
    # def test_light_theme1(self,txt):
    #     db = Views_pg(self.driver)
    #     db.navigate_to_lighttheme()
    #     ut = Utils(self.driver)
    #     ut.enter_text_in_ele(db.hint_text_ele,txt)
    #     ut.took_screenshot(path=f'{self.folder}_testHintTextbox_{txt}.png')


    def test_light_theme_2(self):
        db =Views_pg(self.driver)
        db.navigate_to_lighttheme()
        ut = Utils(self.driver)
        print(1111122223333)
        ut.clicking_on_ele(db.check_box1_ele)
        ut.clicking_on_ele(db.check_box2_ele)
        ut.clicking_on_ele(db.radio_button1_ele)
        time.sleep(2)
        ut.clicking_on_ele(db.radio_button2_ele)
        ut.clicking_on_ele(db.dropdown_ele)
        time.sleep(0.5)
        ut.clicking_on_ele(db.dropdown_options)
        time.sleep(3)
        l = self.driver.find_elements(*db.dropdown_options)
        print(1,l)
        # # l = ut.elements_list(db.dropdown_options)
        # print(1111,l)
        # # l[0].click()
        # for i in l:
        #     ut.clicking_on_ele(db.dropdown_ele)
        #     i.click()


