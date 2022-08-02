from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# When ready to do the challenge!
# caps = {"headspin:capture": True,
#         "headspin:initialScreenSize": {
#             "width": 1920,
#             "height":1080},
#         "browserName": "chrome"}#Copy from headspin page

driver = webdriver.Firefox()


def site_open_press_button():
    """opens 'the internet' and presses the Add Remove button"""
    try:
        wait = WebDriverWait(driver, 3)
        driver.get('https://the-internet.herokuapp.com')
        dyna_load = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Dynamic Loading")))
        assert dyna_load is not None, "This is Asserting that 'Dynamic Load button' by LINK_TEXT didn't work!!!"
        dyna_load.click()
        print('Dynamic load pressed')

    except NoSuchElementException:  # TimeoutException:
        print("Couldn't find the Dynamic Loading button!")


def second_selection_press():
    """Pressing the second selection on the """
    try:
        wait = WebDriverWait(driver, 5)
        second_press = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Example 2:')))
        assert second_press is not None, "This is Asserting the 'Example 2 button Text' by LINK_TEXT didn't work!!!"
        second_press.click()
        print('Example 2 pressed')

    except NoSuchElementException:
        print('Example 2 Element not found!')


def the_start_button():
    """locating and pressing the new start button"""
    try:
        wait = WebDriverWait(driver, 3)
        start_button_pressed = wait.until(EC.presence_of_element_located((By.XPATH,
                    "//button[normalize-space()='Start']"))).click()
        assert start_button_pressed is not None, "This is Asserting the 'Start button' by XPATH didn't work!!!"
        start_button_pressed.click()
        print('Start button pressed')

    except NoSuchElementException:
        print("Couldn't find the start button")


def checking():
    """Checking the presents of the expected Hello World!"""
    wait = WebDriverWait(driver, 1)
    try:
        text_element = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//h4[contains(text(),'Hello World!')]")
            ))
        dyna_load = text_element.text
    except TimeoutException:
        print("The 'text_element' has not yet been found")
        checking()
    else:
        assert 'Hello World!' in dyna_load, "'Hello World!', was not found in dyna_load!!"
        print(dyna_load)


def goto_home():
    """Return to the home page"""
    wait = WebDriverWait(driver, 3)
    driver.get('https://the-internet.herokuapp.com')


site_open_press_button()
second_selection_press()
the_start_button()
checking()
goto_home()
driver.quit()

