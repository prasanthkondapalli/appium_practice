import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Set desired capabilities using options
@pytest.fixture()
def setup_and_tear(request):

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.app = "/home/prasanth/PycharmProjects/appium_practice/apps/ApiDemos-debug.apk"
    options.device_name = "RZCWA00RN4T"
    options.automation_name = "UiAutomator2"
    driver = webdriver.Remote("http://localhost:4723", options=options)
    request.cls.driver = driver
    yield
    driver.quit()

