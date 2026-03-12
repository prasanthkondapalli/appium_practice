import pytest
from utils.utilities import Utils
from pages.views_pg_flow.gallery import Gallery

@pytest.mark.usefixtures("setup_and_tear")
class Test_gallery:


    def test_navigate_photos(self):
        gl=Gallery(self.driver)
        ut=Utils(self.driver)
        gl.navigate_to_gallery()
        gl.select_photos()
        if ut.bool_element_found(gl.photos_loc):
            ut.took_screenshot('./reports/gallery.png')
        else:
            assert False,"error is occurred"

    def test_vscroll(self):
        gl =Gallery(self.driver)
        ut= Utils(self.driver)
        gl.navigate_to_gallery()
        gl.select_photos()
        gl.swipe_to_images_list()
        ut.took_screenshot('./reports/images.png')