import numpy as np
from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as timeOut
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
#     'deviceName': '<device name from automation config>',
#     'udid': '<udid from automation config>',
#     'headspin:capture': True,
# }

# driver = webdriver.Remote(
#     command_executor='https://dev-us-pao-0.headspin.io:7045/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
#     desired_capabilities=caps # CAPS # Swap for APPIUM when in local
# )
#
wait = WebDriverWait(driver, 5)
globalScreenDimension = driver.get_window_rect()
# screen_dimensions = (driver.get_window_rect())


def select_graphics():
    """Pressing the graphics selection in the APIDemos android app"""
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, "Graphics"))).click()


def finger_paint():
    """swipe down to find then select Finger Paint"""
    scroll = ActionBuilder(driver)
    finger = scroll.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration=0, x=100, y=500) # check points with appium desktop
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=0, y=-500, origin="pointer") # check points with appium desktop
    finger.create_pointer_up(MouseButton.LEFT)
    scroll.perform()

    try:
        goto_finger_paint = wait.until(EC.presence_of_element_located(
            (MobileBy.ACCESSIBILITY_ID, 'FingerPaint'))).click()
        # assert ??? Do I need to assert this???
    except EnvironmentError:
        print('Finding finger paint timed out')


# screen_dimensions = (driver.get_window_rect())
print(globalScreenDimension)


def find_center():
    """Half of the screen height to find the centre"""
    center = {'x': None, 'y': None}
    x = int(globalScreenDimension.get('width') / 2)
    y = int(globalScreenDimension.get('height') / 2)
    center = {'x': x, 'y': y}
    return center
# show_center = find_center()
# print(show_center)


def radius_width():
    """Half of the screen width to find the centre"""
    r_width = float(globalScreenDimension.get('width') / 2)
    # print('r_width = ', r_width)
    screen_radius = float((r_width / 100) * 80)
    # print('screen_radius = ', screen_radius)
    return screen_radius  # r_width
# show_radius_width = radius_width()
# print(show_radius_width)


globalCenter = find_center()
print('Global Center =', globalCenter)
globalRadius = radius_width()
print('Global Radius =', globalRadius)
globalSTEPS = []
for i in range(3):
    globalSTEPS.append(i)
print('Global STEPS =', globalSTEPS)
globalStep = int()
print('Global Step =', globalStep)


class DrawCircle():
    """Taking the class approach, center & radius come from function but steps is an int used when calling the class"""
    # screen_dimensions = globalScreenDimension
    point = {'x': float(), 'y': float()}
    new_point = {'x': float(), 'y': float()}
    move = {'x': None, 'y': None}

    def __init__(self, center, radius, steps, step):
        """Initiate the class attributes when the class is called"""
        self.center = globalCenter
        self.radius = globalRadius
        self.steps = globalSTEPS
        self.step = globalStep

    def __repr__(self):
        return (f'{self.center} '
                f'{self.radius} '
                f'{self.steps} static vars ')

    def get_point_on_circle(self):
        """Lets make the points for the circle!!!"""
        s = globalStep
        ts = int(len(globalSTEPS))
        rad = globalRadius
        # pointer = {'x': None, 'y': None}

        theta = (2 * np.pi) * (s / ts)
        xval = float(np.floor(np.cos(theta) * rad))
        yval = float(np.floor(np.sin(theta) * rad))
        self.point['x'] = xval
        self.point['y'] = yval
        return self.point

    def move_to(self):
        """Moves to the next position on the circle"""
        step = globalStep
        move = self.move
        """Move to the next point on the circle"""
        # print('globalStep in move_to, is', globalStep)
        global_steps_length = int(len(globalSTEPS))
        print('global_steps_length =', global_steps_length)
        for item in range(globalStep + 1, global_steps_length):
            print('globalStep in move_to after addition =', globalStep, 'inside of move_to range!')
            self.move = DrawCircle.get_point_on_circle(item)  # I think this is because step not called yet!!!????!!!
            print(item)
        else:
            pass

    def draw_the_circle(self):
        """drawing the circle in steps"""
        step = globalStep
        steps = globalSTEPS
        print('step =', step)
        print(type(step))
        # point = {self.point}  # {'x': float(), 'y': float()}
        # new_point = {self.new_point}  # {'x': None, 'y': None}
        point = DrawCircle.get_point_on_circle(self)

        def swiping():
            """Adds all the swipe actions to the screen!"""
            swipe = ActionBuilder(driver)
            finger = swipe.add_pointer_input(POINTER_TOUCH, "finger")
            self.point = DrawCircle.get_point_on_circle()  # 0
            finger.create_pointer_move(duration=250, x=point['x'], y=point['y'])
            finger.create_pointer_down(MouseButton.LEFT)
            new_point = (DrawCircle.move_to())  # globalStep
            new_point.values()
            finger.create_pointer_move(duration=250, x=new_point['x'], y=new_point['y'], origin="pointer")
            finger.create_pointer_up(MouseButton.LEFT)
            swipe.perform()
            print(new_point)

            for item in range(int(len(globalSTEPS))):
                # step = globalStep
                point = DrawCircle.get_point_on_circle(self)
                swipe = ActionBuilder(driver)
                finger = swipe.add_pointer_input(POINTER_TOUCH, "finger")
                finger.create_pointer_move(duration=0, x=point['x'], y=point['y'])
                finger.create_pointer_down(MouseButton.LEFT)
                new_point = DrawCircle.move_to(self)  # testing
                new_point = DrawCircle.move_to(self)  # testing
                new_point = DrawCircle.move_to(self)  # testing
                new_point = DrawCircle.move_to(self)  # testing
                print('new_point in item in range=', new_point)
                finger.create_pointer_move(duration=250, x=new_point['x'], y=new_point['y'], origin="pointer")
                finger.create_pointer_up(MouseButton.LEFT)
                swipe.perform()
            print('The for item circle is complete!!!!')
    # draw_the_circle()

    # print("Point in item in range =", point)
    # print("New_point in item in range", new_point)
    # point.values['x'], ['y'] == new_point  # create a small function for this this and then call it in
    # here!
    print('The circle is finished')


select_graphics()
finger_paint()
draw_it = DrawCircle(globalCenter, globalRadius, globalSTEPS, globalStep)
draw_it.draw_the_circle(self)  # This doesn't work because I've split draw_the_circle & swipe!!!


# point = DrawCircle.get_point_on_circle(0)
# print(point)


# DrawCircle(ctr, rads, stps)

# DrawCircle

# New_point

# find_centre(screen_dimensions) = returns screen_redius
# move to first point, # touch down
    # first_point = get_point_on_circle(0, steps, center, screen_radius)
    # point == first_point
        # touch down
        # swipe = ActionBuilder(driver)
        # finger = swipe.add_pointer_input(POINTER_TOUCH, "finger")
        # finger.create_pointer_move(duration=0, x=point[0], y=point[y])
        # finger.create_pointer_down(MouseButton.LEFT
        # step += 1
        # new_point = get_point_on_circle(step, steps, origin, radius)
        # finger.create_pointer_up(MouseButton.LEFT)
        # swipe.perform()





# for point in rest of points
#     move to point
# touch up
# perform
#
# step = 0
# move to get_point_on_circle(step)
# for i in range(step + 1, steps):
#    move to get_point_on_circle(i)