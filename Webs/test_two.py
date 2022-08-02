from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

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
        start_button_pressed = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example:nth-child(2) div:nth-child(4) > button:nth-child(1)")))
        assert start_button_pressed is not None, "This is Asserting the 'Start button' by CSS_SELECTOR didn't work!!!"
        start_button_pressed.click()
        print('Start button pressed')

    except NoSuchElementException:
        print("Couldn't find the start button")

# show_me_path = str(driver.find_elements_by_xpath("//button[@onclick='addElement()']/button"))
# text_element = wait.until(EC.presence_of_element_located(
#         (By.XPATH, "//h4[contains(text(),'Hello World!')]")
#         ))
#     t1= text_element.text

# text_element = wait.until(EC.presence_of_element_located(
#         (By.XPATH, "//h4[contains(text(),'Hello World!')]")
#         ))
#     t1= text_element.text
#
#     assert 'Hello World!' in t1


def get_data(finish_element,expectext):
    """getting the text of finish element"""
    finish_text = str(finish_element)
    expectext = str(expectext)

    def checking():
        """Keep checking until the text we want is found"""
        while expectext not in finish_text:
            print(expectext)
            print(finish_text)
            finish_find()
        else:
            print('OK expectext not found in checking')

            pass
    print('finish_text in get_data', finish_text)


def finish_find():
    """Looking for the id=finish and the Hello World! text"""
    try:
        wait = WebDriverWait(driver, 1)
        finish_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Hello World!')]")))
        return finish_element
    except TimeoutException:
        print('waiting for finish element')
        # finish_element = 'Nope'


site_open_press_button()
second_selection_press()
the_start_button()
find_it = finish_find()

got_data = get_data(find_it, 'Hello World!')
print(got_data)

# driver.quit()

# show_me_path = str(driver.find_elements_by_xpath("//button[@onclick='addElement()']/button"))
# text_element = wait.until(EC.presence_of_element_located(
#         (By.XPATH, "//h4[contains(text(),'Hello World!')]")
#         ))
#     t1= text_element.text
#
#     assert 'Hello World!' in t1
#     print('Text: Hello World! is part of dymanic load elements')
#         driver = webdriver.Firefox()
#         driver.get('https://pythonbasics.org')
#         timeout = 3
#         try:
#             element_present = EC.presence_of_element_located((By.ID, 'main'))
#             WebDriverWait(driver, timeout).until(element_present)
#         except TimeoutException:
#             print("Timed out waiting for page to load")
#         finally:
#             print("Page loaded")
# See https://youtu.be/Ho7zzgfh4bQ

