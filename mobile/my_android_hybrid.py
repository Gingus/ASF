import time
from os import path
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

# CAPS = {
#     'platformName': 'Android',
#     'automationName': 'UiAutomator2',
#     'appPackage': 'io.cloudgrey.the_app',
#     'appActivity': 'io.cloudgrey.the_app.MainActivity',
#     'deviceName': 'SM-G973U1',
#     'udid': 'RF8MB031PML',
#     'headspin:capture': True,
#     'headspin:autoDownloadChromedriver': True,
# }
#
# driver = webdriver.Remote(
#     command_executor='https://dev-us-pao-0.headspin.io:7045/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
#     desired_capabilities=CAPS  # CAPS # Swap for APPIUM when in local
# )

CAPS = {
    'platform': 'Android',
    'deviceName': 'pixel_4',
    'automationName': 'UiAutomator2',
    'app': APP,
    'appPackage': 'io.cloudgrey.the_app',
    'appActivity': 'io.cloudgrey.the_app.MainActivity',
    'WebDriver': 'chrome'
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

# app = path.join(CUR_DIR, 'TheApp.apk')
# app_id = 'io.appium.android.apis'

# 'browserName': 'chrome',

the_internet = 'https://the-internet.herokuapp.com'


class WebViewActive(object):
    """Wait until web context is available """
    def __call__(self, driver):
        for context in driver.contexts:
            if context != 'NATIVE_APP':
                driver.switch_to.context(context)
                return True
        return False


# class AppViewActive(object):
#     """Wait until web context is available """
#     def __call__(self, driver):
#         for context in driver.contexts:
#             if context != 'WEBVIEW_io.cloudgrey.the_app':
#                 driver.switch_to.context(context)
#                 return True
#         return False


def tapping_point(tap_time, tap_x, tap_y):
    """pressing at 'co-ord' for 'time' amount of time in milliseconds!
    , can be used for a long press!"""
    t_time = int(tap_time)
    tap_x = int(tap_x)
    tap_y = int(tap_y)
    tap = ActionBuilder(driver)
    finger1 = tap.add_pointer_input(POINTER_TOUCH, "finger")
    finger1.create_pointer_move(duration=tap_time, x=tap_x, y=tap_y)
    finger1.create_pointer_down(MouseButton.LEFT)
    finger1.create_pause(t_time)
    finger1.create_pointer_up(MouseButton.LEFT)
    tap.perform()


# 1. Launch TheApp
# done already because the CAPS setting 'bundleId': 'io.cloudgrey.the-app'

# 2. Go to the 'Webview Demo'
# Test on android just to get the menu items required actions before starting the challenge
try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Webview Demo'))).click()
    print('Web view has been clicked!')
except TimeoutException:
    print("Accessibility ID didn't work!")
    # driver.quit()

# 3. Attempt to navigate to https://the-internet.herokuapp.com using the input
# field and the 'Go' button.
try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.EditText[@content-desc="urlInput"]'))).send_keys(the_internet)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'navigateBtn').click()
    time.sleep(3)
except TimeoutException:
    print("XPATH not found so couldn't attempt to send keys on mobile layer!")

# 4. Handle the resulting alert.
try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'android:id/alertTitle')))
    print('Found alert, now press the OK button!')
except TimeoutException:
    print("ID not found so couldn't try to assert the text of the warning pop up!")
    pass

# click ok on the alert to clear it
try:
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ID, 'android:id/button1'))).click()
    print('Alert cleared!')
    wait.until(WebViewActive())
except TimeoutException:
    print("The Ok button couldn't be found to clear the Alert!")
    # driver.quit()

# ctxs = str
# ctxs = driver.context
# print(ctxs)
# tapping_point(0, 360, 450)

# 5. Using the Context API and all the Selenium commands you have learned,
#    automate the same "login/logout" flow as you did in the module on web
#    automation with Selenium (unit 7.6). Refer to that challenge for the
#    specific details of the web automation steps to take within the webview. (See Below)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(WebViewActive())
    # driver.switch_to.context("WEBVIEW_chrome")
except TimeoutException:
    print("WebDriverActive call didn't work!")

ctxs = driver.context
print(ctxs, 'after WebViewActive call attempt!')

try:
    wait = WebDriverWait(driver, 30)
    wait.until(WebViewActive())
    text_1 = driver.find_element(By.XPATH, "//h1[text()='Please navigate to a webpage']").text
    print(text_1)
    driver.get(the_internet)
    # driver.get('https://the-internet.herokuapp.com')
    # driver.find_element(MobileBy.ACCESSIBILITY_ID, 'navigateBtn').click()
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')))
    form_auth_link.click()

    username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
    username.send_keys('tomsmith')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Logout'))).click()

    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/login'))
    flash = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#flash')))

    assert 'logged out' in flash.text
    print(flash)
    print(driver.current_url)
except TimeoutException:
    print("WebDriverActive commands didn't work!")

# 6. Tap the 'Clear' button in the native UI
ctxs = driver.context
print(ctxs)

driver.switch_to.context("NATIVE_APP")
ctxs = driver.context
print(ctxs)
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'clearBtn'))).click()
    time.sleep(3)
except TimeoutException:
    print("Clear button not found!")

driver.quit()
