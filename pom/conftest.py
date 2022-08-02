from os import path
import pytest
from appium import webdriver
from pom.views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.apk')
# .abspath("C:/Users/gingu/PycharmProjects/asf/TheApp.apk/")
# print(APP) # Use temporarily to find the file location to use in appium to find elements
# exit() # Use temporarily to find the file location to use in appium to find elements
APPIUM = 'http://localhost:4723'


@pytest.fixture
def driver():
    """Abstracting driver and quit"""
    CAPS = {
        'platform': 'Android',
        'deviceName': 'pixel_4',
        'automationName': 'UiAutomator2',
        'app': APP,
        }

    driver = webdriver.Remote(
        command_executor=APPIUM,
        desired_capabilities=CAPS
        )
    yield driver
    # execute quite after being used
    driver.quit()


@pytest.fixture
def home(driver):
    """Some line"""
    return HomeView(driver)
