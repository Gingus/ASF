from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# CUR_DIR = path.dirname(path.abspath(__file__))
# APP = path.join(CUR_DIR, 'TheApp.apk')
# # print(APP) # Use temporarily to find the file location to use in appium to find elements
# # exit() # Use temporarily to find the file location to use in appium to find elements
# APPIUM = 'http://localhost:4723'
CAPS = {
    'deviceName': 'iPhone 11 Pro Max',
    'udid': '00008030-001535310E28802E',
    'automationName': 'XCUITest',
    'platformVersion': '14.2',
    'platformName': 'iOS',
    'bundleId': 'io.cloudgrey.the-app',
    'headspin:capture': True
}

driver = webdriver.Remote(
    command_executor='https://dev-us-pao-0.headspin.io:7044/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
    desired_capabilities=CAPS
)

wait = WebDriverWait(driver, 10)

# try:
#     # time.sleep(4)
#     wait.until(EC.presence_of_element_located(
#         (MobileBy.ACCESSIBILITY_ID, "login"))).click()
#     press_username = wait.until(EC.presence_of_element_located(
#         (MobileBy.ACCESSIBILITY_ID, "username")))
#     print(driver.page_source)
#     pass
# finally:
#     driver.quit()


def add_details(user, passwd):
    """Adding details user and password details for the login screen"""
    # wait = WebDriverWait(driver, 5)
    user = str(user)
    passwd = str(passwd)
    press_username = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "username")))
    press_username.click()
    user_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "username")))
    user_text.send_keys(user)

    press_passwd = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "password")))
    press_passwd.click()
    passwd_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "password")))
    passwd_text.send_keys(passwd)

    login_press = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'loginBtn')))
    login_press.click()


login_screen = wait.until(EC.presence_of_element_located(
    (MobileBy.ACCESSIBILITY_ID, 'Login Screen')))
login_screen.click()


try:
    wait = WebDriverWait(driver, 10)
    alerted = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Login Screen')))
    add_details(user='notMe', passwd='wrong')
    alerted.click()
    alert_press_ok = wait.until(EC.presence_of_element_located(
        (MobileBy.NAME, "OK"))).click()
    add_details(user='alice', passwd='mypassword')
    driver.find_element(MobileBy.CLASS_NAME, 'XCUIElementTypeStaticText')
    print(driver.page_source)

    # driver.find_element(MobileBy.XPATH, '//XCUIElementTypeOther[@Label="Webview Demo"]')
    pass
finally:
    driver.quit()