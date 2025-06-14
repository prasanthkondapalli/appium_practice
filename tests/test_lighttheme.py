import pytest, time
from utils.utilities import Utils
from pages.views_page import Views_pg

@pytest.mark.usefixtures("setup_and_tear")
class Testlighttheme:
    folder = r'./reports/'

    @pytest.mark.parametrize("txt",["txt1",'test 123',12334])
    def test_light_theme1(self,txt):
        db = Views_pg(self.driver)
        db.navigate_to_lighttheme()
        ut = Utils(self.driver)
        ut.enter_text_in_ele(db.hint_text_ele,txt)
        ut.took_screenshot(path=f'{self.folder}_testHintTextbox_{txt}.png')

