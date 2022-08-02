from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
# import time


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
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'messageInput'))).send_keys('Hello')
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
    saved_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Hello'))).text
    assert saved_text == 'Hello', "The saved_text was not equal to 'Hello'"
    driver.back()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    # saved_text = wait.until(EC.presence_of_element_located(
    #     (MobileBy.ACCESSIBILITY_ID, 'savedMessage'))).text
    saved_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Hello'))).text
    assert saved_text == 'Hello', "The saved_text was not equal to 'Hello2'"
    # driver.find_element(MobileBy.CLASS_NAME, 'android.widget.TextView')
    # print(driver.page_source)
    # driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@Text="Webview Demo"]')
finally:
    driver.quit()