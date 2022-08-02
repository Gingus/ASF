from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TOE
from selenium.common.exceptions import NoSuchElementException as NSEE


# CUR_DIR = path.dirname(path.abspath(__file__))
# APP = path.join(CUR_DIR, 'TheApp.apk')

# APPIUM = 'http://localhost:4723' # Swap to this to run in local
# When running locally
# CAPS = {
#     'platform': 'Android',
#     'deviceName': 'pixel_4',
#     'automationName': 'UiAutomator2',
#     'app': APP,
# }

caps = {
    'deviceName': 'iPhone 11 Pro Max',
    'udid': '00008030-001535310E28802E',
    'automationName': 'XCUITest',
    'platformVersion': '14.2',
    'platformName': 'iOS',
    'bundleId': 'io.cloudgrey.the-app',
    'headspin:capture': True
}

# driver = webdriver.Firefox() # when testing web stuff and not android
driver = webdriver.Remote(
    command_executor='https://dev-us-pao-0.headspin.io:7044/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
    desired_capabilities=caps  # CAPS # Swap for APPIUM when in local
)

wait = WebDriverWait(driver, 5)


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
    user_text.send_keys('\b', '\b', '\b', '\b', '\b', user+'\n')

    press_passwd = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "password")))
    press_passwd.click()
    passwd_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "password")))
    passwd_text.send_keys('\b', '\b', '\b', '\b', '\b', passwd+'\n')

    login_press = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'loginBtn')))
    login_press.click()


login_screen = wait.until(EC.presence_of_element_located(
    (MobileBy.NAME, 'Login Screen')))
login_screen.click()


def wrong_details():
    """Attempt login with incorrect details"""
    add_details('notMe', 'wrong')
    try:
        alerted = wait.until(EC.presence_of_element_located(
            (MobileBy.NAME, "Invalid login credentials, please try again"))).text
        print(alerted)
        assert alerted == 'Invalid login credentials, please try again', \
            'Invalid login has not been asserted, check alerted str assertion!'
        alert_press_ok = wait.until(EC.presence_of_element_located(
                (MobileBy.ACCESSIBILITY_ID, "OK"))).click()
    except TOE:
        print('There was no alert message and you have timed out!')
        driver.quit()

    except NSEE:
        print('the wrong username was not found!')
        driver.quit()

    else:
        print("Passed")
        pass


def add_correct():
    """Trying the correct details this time"""
    add_details('alice', 'mypassword')
    try:
        see_alice = wait.until(EC.presence_of_element_located(
            (MobileBy.ACCESSIBILITY_ID, "You are logged in as alice"))).text
        print(see_alice)
        assert 'alice' in see_alice, \
            'Invalid login has not been asserted, check see_alice str assertion!'
    except TOE:
        print("Nope the alice assertion didn't work!")
        driver.quit()
    else:
        print("Passed")
        pass


def alice_logs_out():
    """Alice presses the Logout button"""
    try:
        alice_press_logout = wait.until(EC.presence_of_element_located(
            (MobileBy.ACCESSIBILITY_ID, "Logout")))
    except TOE:
        print('There was no Logout button located and you have timed out!')
        driver.quit()
    else:
        print('switched to Logout!')
        alice_press_logout.click()
        pass


def check_username():
    """Lastly checking the username field is back to what it was!"""
    # wait = WebDriverWait(driver, 3)
    check_user = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "username")))
    # check_text = wait.until(EC.presence_of_element_located(
    #     (MobileBy.ACCESSIBILITY_ID, "username"))).text
    print('The username field is present again!')


wrong_details()
add_correct()
alice_logs_out()
check_username()
driver.quit()