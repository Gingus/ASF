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
        # print('Dynamic load pressed')

    except NoSuchElementException:  # TimeoutException:
        print("Couldn't find the Dynamic Loading button!")
    print('site_open_press_button(), done!')


def select_iframe_button():
    """In the new Frames page, look for 'iFrame' and press it!"""
    try:
        wait = WebDriverWait(driver, 3)
        iframe_button = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "iFrame")))
        assert iframe_button is not None, "This is Asserting that 'Dynamic Load button' by LINK_TEXT didn't work!!!"
        # print(iframe_button)
        iframe_button.click()
        # print('Dynamic load pressed')
    except TimeoutException:
        print("The iFrame button has not yet been found")
    else:
        print("iframe button pressed in 'select_iframe_button'")


def check4_iframe_page():
    """Checking the iframe page loaded only!"""
    wait = WebDriverWait(driver, 2)

    try:
        iframe_page = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h3[normalize-space()='An iFrame containing the TinyMCE WYSIWYG Editor']")))
        assert iframe_page is not None, "This is Asserting that 'Dynamic Load button' by XPATH didn't work!!!"
        # print('iFrame page found by header text')
    except TimeoutException:
        print("The iFrame application has not yet been found after 3 seconds")
    else:
        print('check4_iframe_page is done, iFrame page found by header text')
        pass


def select_file_add():
    """First finding and then pressing 'File' menu option, then pressing the 'New Document' selection"""
    wait = WebDriverWait(driver, 2)
    try:
        file_el = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='File']")))
        assert file_el is not None, "This is Asserting that 'File option' on the iFrame page, could not be found!!!"
        file_el.click()

    except TimeoutException:
        print("The iFrame page, File option has not yet been found after 2 seconds")
    else:
        print('select_file_add done, iframe/File/New Document option found and pressed which clears the text field!')


def sel_new_doc():
    """Select file-new"""
    wait = WebDriverWait(driver, 2)
    try:
        new_doc = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@title='New document']")))
        assert new_doc is not None, "This is Asserting that 'New Option' on the iFrame page, could not be found!!!"
        new_doc.click()
    except TimeoutException:
        print('New Doc Selection was not found!')


def switch_to_iframe():
    """Switch from the New document button to the text area and entering text"""
    wait = WebDriverWait(driver, 1)
    try:
        driver.switch_to.frame("mce_0_ifr")
        text_area = wait.until(EC.presence_of_element_located((By.XPATH, "//body[@id='tinymce']")))
        text_area.send_keys("Hello from Automation!")
        show_area = text_area.text
        # print(show_area) #This is where I had gone wrong!!!
    except TimeoutException:
        print("Timeout raised when trying to find 'mce_0_ifr'!")


def show_me():
    """Showing the assertion of the text in tinymce"""
    wait = WebDriverWait(driver, 1)
    try:
        text_area_again = driver.find_element(By.XPATH, "//body[@id='tinymce']").text # driver.find_element has the
        # all important .text to get the value!
        print('text_area_again =', text_area_again)
        assert 'Hello from Automation!' in text_area_again, "The text in the text area doesn't match!"
    except TimeoutException:
        print("Timeout raised when trying to find 'mce_0_ifr', again!")


def goto_home():
    """Return to the home page"""
    wait = WebDriverWait(driver, 3)
    driver.get('https://the-internet.herokuapp.com')


site_open_press_button()
select_iframe_button()
check4_iframe_page()
select_file_add()
sel_new_doc()
switch_to_iframe()
show_me()
goto_home()
driver.quit()
