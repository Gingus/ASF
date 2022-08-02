import time
# from os import path
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton

# CUR_DIR = path.dirname(path.abspath(__file__))
# APP = path.join(CUR_DIR, 'TheApp.apk')
# APPIUM = 'http://localhost:4723'

CAPS = {
    'deviceName': 'iPhone 11 Pro Max',
    'udid': '00008030-001535310E28802E',
    'automationName': 'XCUITest',
    'platformVersion': '14.2',
    'platformName': 'iOS',
    'bundleId': 'io.cloudgrey.the-app',
    'headspin:capture.video': True,
}

# "headspin:capture": True # Needs putting in when ready!

driver = webdriver.Remote(
    command_executor='https://dev-us-pao-0.headspin.io:7044/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
    desired_capabilities=CAPS  # CAPS # Swap for APPIUM when in local
)


the_internet = 'https://the-internet.herokuapp.com'


class WebViewActive(object):
    """Wait until web context is available """
    def __call__(self, driver):
        for context in driver.contexts:
            if context != 'NATIVE_APP':
                driver.switch_to.context(context)
                return True
        return False


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
        (MobileBy.XPATH, '//XCUIElementTypeTextField[@name="urlInput"]')))
    text_field.send_keys(input_url)

    # To Click the Go Btn
    btn_go = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'navigateBtn')
    btn_go.click()

    # Waiting for the pop up to load properly.
    wait.until(EC.presence_of_element_located(
    (MobileBy.ACCESSIBILITY_ID, 'OK')
    ))

    # To capture alert text
    alert_capture = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'OK')

    #Accept the alert
    alert_capture.click()

    #Switch to Webview
    wait.until(WebViewActive())

    # Will need to reach this point then check for the text_1 locator strategy!
    # text_1 = driver.find_element(By.XPATH, "//h1[text()='Please navigate to a webpage']")
    # print(text_1)

    # tapping_point(500, 208, 467)
    ctxs = driver.context
    print(ctxs)

    time.sleep(3)
    driver.hide_keyboard()

    # time.sleep(3)
    #Launch the URL
    driver.get("https://the-internet.herokuapp.com")
    # WebDriverWait(driver, 30).until(EC.url_to_be('https://the-internet.herokuapp.com'))
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
    time.sleep(3)

finally:
    driver.quit()
