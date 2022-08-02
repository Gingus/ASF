import time
# from os import path
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton

# CUR_DIR = path.dirname(path.abspath(__file__))
# APP = path.join(CUR_DIR, 'TheApp.apk')
# APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'appPackage': 'io.cloudgrey.the_app',
    'appActivity': 'io.cloudgrey.the_app.MainActivity',
    'deviceName': 'SM-G973U1',
    'udid': 'RF8MB031PML',
    'headspin:capture': True,
    'headspin:autoDownloadChromedriver': True,
}

driver = webdriver.Remote(
    command_executor='https://dev-us-pao-0.headspin.io:7045/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
    desired_capabilities=CAPS  # CAPS # Swap for APPIUM when in local
)

# CAPS = {
#     'platform': 'Android',
#     'deviceName': 'pixel_4',
#     'automationName': 'UiAutomator2',
#     'app': APP,
#     'appPackage': 'io.cloudgrey.the_app',
#     'appActivity': 'io.cloudgrey.the_app.MainActivity',
#     'WebDriver': 'chrome'
# }

# driver = webdriver.Remote(
#     command_executor=APPIUM,
#     desired_capabilities=CAPS
# )

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

# URL info
input_url = 'https://the-internet.herokuapp.com'

try:
    wait = WebDriverWait(driver, 30)

    # Click the Webview Demo
    ele_click = wait.until(EC.presence_of_element_located(
    (MobileBy.ACCESSIBILITY_ID, 'Webview Demo')
    ))
    ele_click.click()

    # Enter the URL in the Text field
    text_field = wait.until(EC.presence_of_element_located(
    (MobileBy.ACCESSIBILITY_ID, 'urlInput')
    ))
    text_field.send_keys(input_url)

    # To Click the Go Btn
    btn_go = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'navigateBtn')
    btn_go.click()

    # Waiting for the pop up to load properly.
    wait.until(EC.presence_of_element_located(
    (MobileBy.ID, 'android:id/alertTitle')
    ))

    # To capture alert text
    alert_capture = driver.find_element(MobileBy.ID, 'android:id/message').text

    print(alert_capture)

    #Accept the alert

    alert_accept = driver.find_element(MobileBy.ID, 'android:id/button1')
    alert_accept.click()

    # driver.find_element(By.XPATH, "//android.webkit.WebView[@index ='3']").click()

    #Switch to Webview
    wait.until(WebViewActive())

    text_1 = driver.find_element(By.XPATH, "//h1[text()='Please navigate to a webpage']").text
    print(text_1)

    #Launch the URL

    driver.get("http://the-internet.herokuapp.com")


    # Click Form Authentication
    form_auth_link = wait.until(EC.presence_of_element_located(
    (By.LINK_TEXT, 'Form Authentication')
    ))
    form_auth_link.click()

    # Enter username
    username = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, '#username')))

    username.send_keys('tomsmith')

    # Enter Password
    password = driver.find_element(By.CSS_SELECTOR, '#password')

    password.send_keys('SuperSecretPassword!')

    # Click Login
    Login = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    Login.click()

    # Click Logout
    wait.until(EC.presence_of_element_located(
    (By.LINK_TEXT, 'Logout')
    )).click()

    flash = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, '#flash')
    ))

    assert 'logged out' in flash.text

    # Switch back to Native context
    driver.switch_to.context('NATIVE_APP')

    # To Clear the URL in the text field

    btn_clear = wait.until(EC.presence_of_element_located(
    (MobileBy.ACCESSIBILITY_ID, 'clearBtn')
    ))
    btn_clear.click()

finally:
    driver.quit()
