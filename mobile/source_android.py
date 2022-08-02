from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
# print(APP) # Use temporarily to find the file location to use in appium to find elements
# exit() # Use temporarily to find the file location to use in appium to find elements
APPIUM = 'http://localhost:4723'
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

try:
    time.sleep(4)
    print(driver.page_source)
    pass
finally:
    driver.quit()