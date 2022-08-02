from appium import webdriver
from os import getcwd
import time
from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# CUR_DIR = path.dirname(path.abspath(__file__))
# APP = path.join(CUR_DIR, 'ApiDemos.apk')
# APPIUM = 'http://localhost:4723' # Swap to this to run in local
# # When running locally
# CAPS = {
#     'platform': 'Android',
#     'deviceName': 'pixel_4',
#     'automationName': 'UiAutomator2',
#     'app': APP,
# }
# driver = webdriver.Remote(
#     command_executor=APPIUM,
#     desired_capabilities=CAPS
# )

caps = {
  "deviceName": "iPhone 11 Pro Max",
  "udid": "00008030-001535310E28802E",
  "automationName": "XCUITest",
  "platformVersion": "14.2",
  "platformName": "iOS",
  "bundleId": "com.apple.Maps",
  "headspin:capture": True,
}

# "headspin:capture": True # When ready to record!!!!!!!!!!!
# "bundleId": "com.apple.Maps",
# "bundleId": "com.apple.Springboard" Doesn't work!!!
# "bundleId": "com.apple.Preferences" This launches into the settings screen!!!!!!!


driver = webdriver.Remote(
    command_executor='https://dev-us-pao-0.headspin.io:7044/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
    desired_capabilities=caps  # CAPS # Swap for APPIUM when in local
)
# driver.terminate_app('com.apple.Maps')
wait = WebDriverWait(driver, 10)
# WebDriverWait(driver, 30)
directory = '%s/' % getcwd() # Need something else for ios
file_name = 'screenshot.png'
screen_dimension = driver.get_window_rect()
stan_park = {'x': '', 'y': ''}


def tapping_point(tap_time, tap_x, tap_y):
    """pressing at 'co-ord' for 'time' amount of time in milliseconds!
    , can be used for a long press!"""
    t_time = int(tap_time)
    tap_x = int(tap_x)
    tap_y = int(tap_y)
    tap = ActionBuilder(driver)
    finger1 = tap.add_pointer_input(POINTER_TOUCH, "finger")
    finger1.create_pointer_move(duration=tap_time, x=tap_x, y=tap_y) #  x=195, y=223)# Check for co-ords
    finger1.create_pointer_down(MouseButton.LEFT)
    finger1.create_pause(t_time)
    finger1.create_pointer_up(MouseButton.LEFT)
    tap.perform()


def stanley_park_location():
    """Getting the screen size and returning a relative position"""
    global stan_park
    x = float(screen_dimension.get('width') / 2)
    y = float((screen_dimension.get('height') / 2) + (screen_dimension.get('height') / 7))
    stan_park['x'] = x
    stan_park['y'] = y
    print('stan park x =', stan_park['x'], '\n',
          'stan park y =', stan_park['y'])


def press_stan_park():
    """Using stanley_park_location and tapping_point"""
    global stan_park
    stanley_park_location()  # this updates 'global stan_park' dict x and y values
    x = stan_park['x']
    y = stan_park['y']
    tapping_point(2500, x, y)  # presses the stan park co-ordinate for 2.5 seconds (I think)
    print('x=', x, 'y=', y)


def swipe_right():
    """swipe down to find then select Finger Paint"""
    scroll = ActionBuilder(driver)
    finger = scroll.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration=0, x=50, y=360)
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=289, y=-360, origin="pointer")
    finger.create_pointer_up(MouseButton.LEFT)
    scroll.perform()


# 1. Launch the Apple Maps app
# starting straight into the app same as in 8.8

# # 2. Search for "Vancouver, BC"
try:
    check_search = wait.until(EC.presence_of_element_located(
    (MobileBy.ACCESSIBILITY_ID, 'Search for a place or address')))
    check_search.click()
except NoSuchElementException:
    print('Could not find search box first try so looking for the close button!')
    driver.terminate_app('com.apple.Maps')
    driver.quit()
    pass
except TimeoutException:
    print('Could not find search box!, Timed out!')
    try:
        check_x = wait.until(EC.presence_of_element_located(
            (MobileBy.ACCESSIBILITY_ID, 'Close'))).click()
        check_search = wait.until(EC.presence_of_element_located(
            (MobileBy.ACCESSIBILITY_ID, 'Search for a place or address')))
        check_search.click()
    except TimeoutException:
        print('Could not find Close button either!, Timed out!')
        driver.terminate_app('com.apple.Maps')
        driver.quit()
        pass

the_dictate_el = driver.find_element_by_accessibility_id('Dictate')
the_dictate_el.send_keys('Vancouver, BC')  # , '\n')

# 3. Tap the appropriate city in the response list
wait = WebDriverWait(driver, 30)
city = driver.find_element(MobileBy.XPATH, "(//XCUIElementTypeStaticText[@name='Vancouver, BC'])[1]")
city.click()
# print('City was clicked!')

# 4. Press and hold the Stanley Park region of the map, until a Stanley Park card
#   pops up
long_press_stan = ActionBuilder(driver)
finger = long_press_stan.add_pointer_input(POINTER_TOUCH, "finger")
finger.create_pointer_move(duration=1000, x=193, y=223)
finger.create_pointer_down(MouseButton.LEFT)
finger.create_pause(3)
# finger.create_pointer_move(duration=3000, x=150, y=177, origin="pointer")
finger.create_pointer_up(MouseButton.LEFT)
long_press_stan.perform()
time.sleep(5)


# 5. Verify the card has appeared
driver.save_screenshot('pop_up.png')  # ###TAKE A SCREEN PICTURE!!!

# 6. Tap outside the card to dismiss it
tapping_point(0, 360, 450)  # Click outside of the card area, to go back to the map()
print('tapped out of the thing')
time.sleep(2)


def zoom_fingers():
    """swipe down to find then select Finger Paint"""
    zooming = ActionBuilder(driver)
    finger = zooming.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration=0, x=193, y=223)
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pause(0.5)
    finger.create_pointer_move(duration=1000, x=0, y=-50, origin="pointer")
    finger.create_pointer_up(MouseButton.LEFT)

    finger1 = zooming.add_pointer_input(POINTER_TOUCH, "finger1")
    finger1.create_pointer_move(duration=0, x=193, y=223)
    finger1.create_pointer_down(MouseButton.LEFT)
    finger1.create_pause(0.5)
    finger1.create_pointer_move(duration=1000, x=0, y=50, origin="pointer")
    finger1.create_pointer_up(MouseButton.LEFT)
    zooming.perform()
    time.sleep(2)


zoom_fingers()

# 8. Take a screenshot of the result of your work (DONE)
driver.save_screenshot('final_screen_output.png')

# driver.terminate_app('com.apple.Maps'), Used whilst testing!
driver.quit()