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
        wait = WebDriverWait(driver, 2)
        driver.get('https://the-internet.herokuapp.com')
        frame_button = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Frames")))
        assert frame_button is not None, "This is Asserting that 'Dynamic Load button' by LINK_TEXT didn't work!!!"
        frame_button.click()
        print('Dynamic load pressed')

    except NoSuchElementException:  # TimeoutException:
        print("Couldn't find the Dynamic Loading button!")


def select_iframe_button():
    """In the new Frames page, look for 'iFrame' and press it!"""
    try:
        wait = WebDriverWait(driver, 1)
        iframe_button = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "iFrame")))
        assert iframe_button is not None, "This is Asserting that 'Dynamic Load button' by LINK_TEXT didn't work!!!"
        # print(iframe_button)
        iframe_button.click()
        # print('Dynamic load pressed')
    except TimeoutException:
        print("The iFrame button has not yet been found")
    else:
        print('iframe button pressed')


def check4_iframe_page():
    """Checking the iframe page loaded only!"""
    wait = WebDriverWait(driver,3)

    try:
        iframe_page = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'An iFrame containing the TinyMCE WYSIWYG Editor')]")))
        assert iframe_page is not None, "This is Asserting that 'Dynamic Load button' by LINK_TEXT didn't work!!!"

    except TimeoutException:
        print("The iFrame page has not yet been found after 3 seconds")
    else:
        print('iframe page found')


def select_file_add():
    """First finding and then pressing 'File' menu option, then pressing the 'New Document' selection"""
    wait = WebDriverWait(driver, 3)
    try:
        file_el = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='File']")))
        assert file_el is not None, "This is Asserting that 'File option' on the iFrame page, could not be found!!!"
        file_el.click()

    except TimeoutException:
        print("The iFrame page, File option has not yet been found after 3 seconds")
    else:
        print('iframe/File option found')


def sel_new_doc():
    """Select file-new"""
    wait = WebDriverWait(driver, 3)
    try:
        new_doc = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@title='New document']")))
        assert new_doc is not None, "This is Asserting that 'New Option' on the iFrame page, could not be found!!!"
        new_doc.click()
        print('New Doc has been pressed')
    except TimeoutException:
        print('New Doc Selection was not found!')


def enter_message():
    """Adding message to the entry field, 'Hello from automation"""
    wait = WebDriverWait(driver, 2)
    try:
        find_field = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@id='mce_0_ifr']")))
        assert find_field is not None, "This is Asserting that 'Entry Field' on the iFrame page, could not be found!!!"
        print('Entry Field has been found')
        find_field.send_keys('Hello from Automation!')
    except TimeoutException:
        print('Entry field was not found!')
    # return find_field


def show_it():
    """Split out the confirmation part"""
    try:
        wait = WebDriverWait(driver, 2)
        find_field = driver.find_element(By.XPATH, "//body[@id='tinymce']").text
        print('Text Captured: ',actual_text)
        assert actual_text == 'Hello from Automation!', 'Still not working!'
        # //iframe[@id='mce_0_ifr']
    except NoSuchElementException:
        print('Element not found')
        pass


def goto_home():
    """Return to the home page"""
    wait = WebDriverWait(driver, 3)
    driver.get('https://the-internet.herokuapp.com')


site_open_press_button()
select_iframe_button()
check4_iframe_page()
select_file_add()
sel_new_doc()
enter_message()
# show_it()
goto_home()
driver.quit()