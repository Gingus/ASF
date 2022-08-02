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

wait = WebDriverWait(driver, 5)


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
        # assert
    finally:
        pass


def find_center(screen_dimensions):
    """Half of the screen height to find the centre"""
    x = int(screen_dimensions.get('width')/2)
    y = int(screen_dimensions.get('height')/2)
    center = {'x': x, 'y': y}
    return center
    # print(screen_y_height)
    # return screen_x_width, screen_y_height, radius


def radius_width(screen_dimensions):
    """Half of the screen width to find the centre"""
    r_width = int(screen_dimensions.get('width')/2)
    screen_radius = int((r_width/100)*90)
    return screen_radius  # r_width 80%


center = find_center()
radius = float(radius_width())
steps = int()

def draw_circle(self, center, radius, steps):
    """draw the circle using the points, centre & screen_radius from above but add number 'steps'"""
    center = center
    def get_point_on_circle(self, step, steps, origin, radius):
        """Lets make the points for the circle!!!"""
        step = int(step)
        steps = int()
        origin = center.values()
        radius = float(radius)
        theta = (2 * np.pi) * (step / steps)
        x = int(np.floor(np.cos(theta) * radius))
        y = int(np.floor(np.sin(theta) * radius))
        new_point = (origin['x'] + x, origin['y'] + y)
        return new_point

    def swipe_action():
        """Making the swipe"""
        point = (x,y)

        def new(x, y):
            """Creating an element with a str key and int elements to the 'my_dict'"""
            x = int(x)
            y = int(y)
            new_element = (x, y)
            return new_element

        def create_element(name, el):
            """Creating an element with a str key and int elements to the 'my_dict'"""
            name = str(name)
            el = int(el)
            new_element = {name: el}
            return new_element
        new_point = (x,y)
        point = get_point_on_circle(0, steps, origin, radius)
        # Drawing the circle
        step = int(0)
        new_point = get_point_on_circle(step, steps, origin, radius)  # get first point


    for the_point in rest_of_points():
        """iterate through the points in the circle"""
        point = get_point_on_circle(step, steps, origin, radius)
        swipe = ActionBuilder(driver)
        finger = swipe.add_pointer_input(POINTER_TOUCH, "finger")  # move to first point, touch down
        finger.create_pointer_move(duration=0, x=point[0], y=point[y])
        finger.create_pointer_down(MouseButton.LEFT
        # step += 1?????
        # move to point
        # new_point = get_point_on_circle(step, steps, origin, radius)
        finger.create_pointer_move(duration=250, x=new_point[0], y=new_point[1], origin="pointer")
        # check points with appium desktop
        finger.create_pointer_up(MouseButton.LEFT
        swipe.perform()
    # touch up
    # perform

    move to get_point_on_circle(step)
    for i in range(step + 1, steps):
       move to get_point_on_circle(i)
#############################
# Draw a line that cuts the circle in half, and whose length is the diameter
# of the circle




def paint_tester():
    """swipe Finger to tes Paint point!"""
    start_p = first_point(origin, rad)
    show_t = start_p.values()
    x1 =
    y1 =

    swipe = ActionBuilder(driver)
    finger = swipe.add_pointer_input(POINTER_TOUCH, "finger")


    finger.create_pointer_move(duration=0, x=x1, y=y1) # check points with appium desktop


    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=0, y=-500, origin="pointer") # check points with appium desktop
    finger.create_pointer_up(MouseButton.LEFT)
    scroll.perform()

# Find the highest and lowest point of the circle, draw a line using these points
# Draw another line that cuts the circle in half, but in the opposite axis
# Find the Leftmost point and and the rightmost point of the circle, draw a line using these points
# Save a screenshot of your masterpiece
# use android screen shot to get a pic, there's nothing in the app!!


# select_graphics()
# finger_paint()
# screen_dimension = driver.get_window_rect()
# origin = find_center(screen_dimension)
# rad = radius_width(screen_dimension)

# print(origin)
# print(radius)
# start_point = first_point(origin, rad)
# show_them = start_point.values()
# print(show_them)


# The circle should be centered on the screen
# yes, I called my drawCircle with a larger number of steps to make it pretty smooth.  That steps was the number of
# times I moved the pointer to a new point on the circle.  The get_point_on_circle function used that number as the
# total steps so that I was dividing the circle into the correct number of steps (think slices of pie).  The "step"
# in get_point_on_circle was which slice of the pie out of the total that I was looking at.

Actions actions = new Actions(driver);
actions.click(element);
actions.perform();

class getPointOnCircle (int step, int totalSteps, Point origin, double radius): {
    double theta = 2 * Math.PI * ((double)step / totalSteps);
    int x = (int)Math.floor(Math.cos(theta) * radius);
    int y = (int)Math.floor(Math.sin(theta) * radius);
    return new Point(origin.x + x, origin.y + y);
}

def drawCircle (AppiumDriver driver, Point origin, double radius, int steps) {
    Point firstPoint = getPointOnCircle(0, steps, origin, radius);

    PointerInput finger = new PointerInput(Kind.TOUCH, "finger");
    Sequence circle = new Sequence(finger, 0);
    circle.addAction(finger.createPointerMove(NO_TIME, VIEW, firstPoint.x, firstPoint.y));
    circle.addAction(finger.createPointerDown(MouseButton.LEFT.asArg()));

    for (int i = 1; i < steps + 1; i++) {
        Point point = getPointOnCircle(i, steps, origin, radius);
        circle.addAction(finger.createPointerMove(STEP_DURATION, VIEW, point.x, point.y));
    }

    circle.addAction(finger.createPointerUp(MouseButton.LEFT.asArg()));
    driver.perform(Arrays.asList(circle));
}