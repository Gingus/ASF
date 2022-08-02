import numpy as np
from appium import webdriver
from os import path
from os import getcwd
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'ApiDemos.apk')
APPIUM = 'http://localhost:4723' # Swap to this to run in local
# When running locally
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

# caps = {
#     'platformName': 'Android',
#     'automationName': 'UiAutomator2',
#     'appPackage': 'io.appium.android.apis',
#     'appActivity': '.ApiDemos',
#     'deviceName': 'SM-G973U1',
#     'udid': 'RF8MB031PML',
#     'headspin:capture': True,
# }
#
# driver = webdriver.Remote(
#     command_executor='https://dev-us-pao-0.headspin.io:7045/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
#     desired_capabilities=caps  # CAPS # Swap for APPIUM when in local
# )

directory = '%s/' % getcwd()
file_name = 'screenshot.png'
wait = WebDriverWait(driver, 5)

step = 0
steps = 32
point = {'x': int(), 'y': int()}
new_point = {'x': int(), 'y': int()}
screen_dimension = driver.get_window_rect()
show_step = []
show_steps = []
the_steps = []

for i in range(steps):
    the_steps.append(int(i))


def select_graphics():
    """Pressing the graphics selection in the APIDemos android app"""
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "Graphics"))).click()


def finger_paint():
    """swipe down to find then select Finger Paint"""
    scroll = ActionBuilder(driver)
    finger = scroll.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration=0, x=100, y=500)
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=0, y=-500, origin="pointer")
    finger.create_pointer_up(MouseButton.LEFT)
    scroll.perform()
    try:
        wait.until(EC.presence_of_element_located(
            (MobileBy.ACCESSIBILITY_ID, 'FingerPaint'))).click()
        #  goto_finger_paint = wait.until(EC.presence_of_element_located(
         #  (MobileBy.ACCESSIBILITY_ID, 'FingerPaint'))).click()
    finally:
        pass


def radius_width():
    """Half of the screen width to find the centre"""
    r_width = float(screen_dimension.get('width')/2)
    screen_radius = float((r_width/100)*40)
    return screen_radius


def find_center():
    """Half of the screen height to find the centre"""
    x = int(screen_dimension.get('width')/2)
    y = int((screen_dimension.get('height')/2)+(screen_dimension.get('height')/7))
    middle = {'x': x, 'y': y}
    return middle


def get_point_on_circle(step, steps, center, radius):
    """Lets make the points for the circle!!!"""
    s = step
    ts = steps
    origin = list(center.values())
    theta = (2 * np.pi) * (s / ts)
    x = int(round(np.floor(np.cos(theta) * radius)))
    y = int(round(np.floor(np.sin(theta) * radius)))
    gp_point = (origin[0] + x, origin[1] + int(y))
    return gp_point


def move_to():
    """Moves to the next position in the  list"""
    global step
    global steps
    for item in range(step, steps):
        step += 1
        return step
    else:
        pass


def point_update(cord):
    """Takes co-ordinates tuple and adds those values to the point dict"""
    new_x = cord[0]
    new_y = cord[1]
    global point
    point['x'] = new_x
    point['y'] = new_y


def new_point_update(cord):
    """Takes co-ordinates tuple and adds those values to the new_point dict"""
    x = cord[0]
    y = cord[1]
    global new_point
    new_point['x'] = x
    new_point['y'] = y


def circle():
    """Start the circle"""
    global step
    global steps
    global point
    global new_point
    first_point = get_point_on_circle(step, steps, center, radius)
    point_update(first_point)
    show_steps.append(first_point)
    move_to()
    swipe_point = get_point_on_circle(step, steps, center, radius)
    show_steps.append(swipe_point)
    new_point_update(swipe_point)
    first_line = ActionBuilder(driver)
    finger = first_line.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration=0, x=point['x'], y=point['y'])
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=new_point['x'], y=new_point['y'], origin="viewport")
    for thing in the_steps:
        move_to()
        swipe_point = get_point_on_circle(step, steps, center, radius)
        show_steps.append(swipe_point)
        new_point_update(swipe_point)
        finger.create_pointer_move(duration=250, x=new_point['x'], y=new_point['y'], origin='viewport')
    finger.create_pointer_up(MouseButton.LEFT)
    first_line.perform()


def quarters(coord):
    """Covert fourths back to dict vals"""
    x = coord[0]
    y = coord[1]
    ret_dict = {'x': x, 'y': y}
    return ret_dict


def draw_cross():
    """Uses the show steps positions and convert to x/y co-ords"""
    global steps
    global center
    global radius
    right = get_point_on_circle(0, steps, center, radius)
    right_coord = quarters(right)
    left = get_point_on_circle(16, steps, center, radius)
    left_coord = quarters(left)
    bottom = get_point_on_circle(8, steps, center, radius)
    bottom_coord = quarters(bottom)
    top = get_point_on_circle(24, steps, center, radius)
    top_coord = quarters(top)
    cross_part = ActionBuilder(driver)
    finger = cross_part.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration=0, x=left_coord['x'], y=left_coord['y'])
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=right_coord['x'], y=right_coord['y'], origin="viewport")
    finger.create_pointer_up(MouseButton.LEFT)
    cross_part.perform()
    cross_part_two = ActionBuilder(driver)
    finger = cross_part_two.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration=0, x=bottom_coord['x'], y=bottom_coord['y'])
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=top_coord['x'], y=top_coord['y'], origin="viewport")
    finger.create_pointer_up(MouseButton.LEFT)
    cross_part_two.perform()


def add_step_steps(step_item, point_item):
    """Appends to show_step and show_steps"""
    show_step.append(step_item)
    show_steps.append(point_item)


select_graphics()
finger_paint()
radius = radius_width()
center = find_center()
circle()
draw_cross()
driver.save_screenshot(directory + file_name)  # ###TAKE A SCREEN PICTURE!!!
driver.quit()