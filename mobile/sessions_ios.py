from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://locahost:4723'

CAPS = {
    'platform': 'ios',
    'platformVersion': '13.6',
    'deviceName': 'iPhone 11',
    'automationName': 'XCUITest',
    'app': APP
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

driver.quit()