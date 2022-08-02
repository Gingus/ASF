from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://locahost:4723'

caps = {
    'deviceName': 'iPhone 11 Pro Max',
    'udid': '00008030-001535310E28802E',
    'automationName': 'XCUITest',
    'platformVersion': '14.2',
    'platformName': 'iOS',
    'bundleId': 'io.cloudgrey.the-app',
    'headspin:capture': True
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=caps
)

try:
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'login Screen')))
    driver.find_element(MobileBy.CLASS_NAME, 'XCUIElementTypeStaticText')
    driver.find_element(MobileBy.XPATH, '//XCUIElementTypeOther[@Label="Webview Demo"]')
    pass
finally:
    driver.quit()