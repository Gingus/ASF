from appium import webdriver
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'
CAPS = {
    'platform': 'Android',
    'deviceName': 'pixel4',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

# try:
#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.presence_of_element_located(
#         (MobileBy.ACCESSIBILITY_ID, 'login Screen')))
#     driver.find_element(MobileBy.CLASS_NAME, 'XCUIElementTypeStaticText')
#     driver.find_element(MobileBy.XPATH, '//XCUIElementTypeOther[@Label="Webview Demo"]')
#     pass
# finally:
#     driver.quit()