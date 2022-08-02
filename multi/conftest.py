from os import path
import pytest
from appium import webdriver
from multi.views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
IOS_APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.app.zip')
ANDROID_APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.apk')
# .abspath("C:/Users/gingu/PycharmProjects/asf/TheApp.apk/")
# print(APP) # Use temporarily to find the file location to use in appium to find elements
# exit() # Use temporarily to find the file location to use in appium to find elements
APPIUM = 'http://localhost:4723'

IOS_CAPS = {
    'platformName': 'iOS',
    'platformVersion': '13.6',
    'deviceName': 'iPhone 11',
    'automationName': 'XCUITest',
    'app': 'APP',
    'platform': IOS_APP,
    }

ANDROID_CAPS = {
    'platformName': 'Android',
    'deviceName': 'pixel_4',
    'automationName': 'UiAutomator2',
    'app': ANDROID_APP,
    }


def pytest_addoption(parser):
    """Adding platform"""
    parser.addoption("--platform", action="store", default="ios")


@pytest.fixture
def platform(request):
    """Makes it so that we can choose between iOS & Android"""
    plat = request.config.getoption('platform').lower()
    if plat not in ["ios", "android"]:
        raise ValueError('--platform value must be ios or android')
    return plat


@pytest.fixture
def driver(platform):
    """Abstracting driver and quit"""
    caps = IOS_CAPS if platform == "iOS" else ANDROID_CAPS
    driver = webdriver.Remote(
        command_executor=APPIUM,
        desired_capabilities=caps
        )
    driver._platform = platform
    yield driver
    # execute quite after being used
    driver.quit()


@pytest.fixture
def home(driver):
    """Some line"""
    return HomeView(driver)
