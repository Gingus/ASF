from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'
CAPS = {
    'platform': 'Android',
    'deviceName': 'pixel_3a',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'login Screen')))
    driver.find_element(MobileBy.CLASS_NAME, 'android.widget.TextView')
    print(driver.page_source)
    driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@Text="Webview Demo"]')
    pass
finally:
    driver.quit()