from os import path
import pytest
from appium import webdriver
from parallel.views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
IOS_APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.app.zip')
ANDROID_APP = path.join(CUR_DIR, 'TheApp.apk')
# app_id = 'io.appium.android.apis'
# .abspath("C:/Users/gingu/PycharmProjects/asf/TheApp.apk/")
# print(APP) # Use temporarily to find the file location to use in appium to find elements
# exit() # Use temporarily to find the file location to use in appium to find elements
APPIUMS = ['http://localhost:4700', 'http://localhost:4701']  # 'http://localhost:4723'

the_internet = 'https://the-internet.herokuapp.com'

IOS_CAPS = [{
    'platformName': 'iOS',
    'platformVersion': '13.6',
    'deviceName': 'iPhone 11',
    'automationName': 'XCUITest',
    'platform': IOS_APP,
    }, {
    'platformName': 'iOS',
    'platformVersion': '13.6',
    'deviceName': 'iPhone 8',
    'automationName': 'XCUITest',
    'platform': IOS_APP,
}]
# 'WebDriver': 'chrome',
# 'browserName': 'chrome',
#     'platformVersion': '11.0',

ANDROID_CAPS = [{
    'platformName': 'Android',
    'deviceName': 'pixel_4',
    'platformVersion': '11',
    'automationName': 'UiAutomator2',
    'app': ANDROID_APP,
    'WebDriver': 'chrome',
    'appPackage': 'io.cloudgrey.the_app',
    'appActivity': 'io.cloudgrey.the_app.MainActivity',
}, {
    'platformName': 'Android',
    'deviceName': 'pixel_3a',
    'platformVersion': '10',
    'automationName': 'UiAutomator2',
    'app': ANDROID_APP,
    'WebDriver': 'chrome',
    'appPackage': 'io.cloudgrey.the_app',
    'appActivity': 'io.cloudgrey.the_app.MainActivity',
}]

#     'browserName': 'chrome',


# DONE 1: define and prepare our test environments
# DONE 2: update conftest to allow for *sets* of environments and not just one
# DONE 3: figure out which pytest worker is asking for a driver
# DONE 4: update driver fixture to parameterize server and caps based on worker id
# DONE 5: ensure that we don't try to run more parallel tests than we should
# def pytest_addoption(parser):


def pytest_addoption(parser):
    """Making it possible for us to run on different platforms"""
    parser.addoption("--platform", action="store", default="iOS")


# @pytest.fixture
# def worker_id(request):
#     """Added to test if this fixes the 'E fixture 'worker_id' not found'"""
#     return request.param

@pytest.fixture
def worker_num(worker_id):
    """Converts the worker_id into an int to match up with No of drivers"""
    print(worker_id)
    if worker_id == 'master':
        worker_id = 'gw0'
    return int(worker_id[2:])


@pytest.fixture
def server(worker_num):
    """Making sure there's not too many servers"""
    if worker_num >= len(APPIUMS):
        raise Exception('Too many workers for the num of Appium servers')
    return APPIUMS[worker_num]


@pytest.fixture
def caps(platform, worker_num):
    """Making sure there's not too many workers"""
    # cap_set = ANDROID_CAPS if platform == 'Android' else IOS_CAPS
    cap_set = IOS_CAPS if platform == 'iOS' else ANDROID_CAPS
    if worker_num >= len(cap_set):
        raise Exception('Too many workers for the num of cap sets')
    return cap_set[worker_num]


@pytest.fixture
def platform(request):
    """Makes it so that we can choose between iOS & Android"""
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be ios or android')
    print('plat =', plat)
    return plat


@pytest.fixture
def driver(server, caps, platform):
    """Abstracting driver and quit"""
    driver = webdriver.Remote(
        command_executor=server,
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

# Starting 2 appium ports at once on ios
# appium -p 4700 --default-capabilities '{"wdaLocalPort": 8100, "wdaLocalPort"; 8200}'
# Starting 2 appium ports at once on android
# appium -p 4723 --default-capabilities '{"SystemPort": 8100, "systemPort": 8200 }'
# appium -p 4700 --default-capabilities '{"SystemPort": 8101, "systemPort": 8201 }'
# or a mix
# appium -p 4700 --default-capabilities '{"wdaLocalPort": 8100, "systemPort": 8200 }'

# to run the simultaneous tests from terminal, pytest -n 2
# appium -p 4700 --default-capabilities "{\"wdaLocalPort\": 8100, \"systemPort\": 8200}"
# appium -p 4701 --default-capabilities "{\"wdaLocalPort\": 8101, \"systemPort\": 8201}"
# This works :)
