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
        form_add_remove = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Add/Remove Elements")))
        form_add_remove.click()
        wait.until(EC.url_to_be('https://the-internet.herokuapp.com/add_remove_elements/'))
        print('Add/Remove found')
        # print(driver.current_url)

    except NoSuchElementException:  # TimeoutException:
        print("Couldn't find the Add/Remove Elements button!")


def click_dynamic_load():
    """Selecting the dynamic loading choice from the main page"""
    try:
        wait = WebDriverWait(driver,3)
        dynamic_load_pressed = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Dynamic Loading")))
        dynamic_load_pressed.click()

    except TimeoutException:
        print('Dynamic load was not found at this time!')


def dynamic_page_loaded():
    """Making sure the page is loaded"""
    try:
        wait = WebDriverWait(driver, 3)
        wait.until(EC.presence_of_element_located(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/h3[1]")

    # except NoSuchElementException:
    #     print("New 'Dynamically Loaded Page Elements' has not yet been found!")



# def check_del_or_press_add():
#     """Use a try/Except check for Delete or press Add button until there are two"""
#     element_count = int(0)
#
#     try:
#         wait = WebDriverWait(driver, 3)
#         form_delete = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Delete")))
#
#     except TimeoutException:
#         # wait = WebDriverWait(driver, 3)
#         print('Delete Button not yet found!')
#         assert TimeoutException
#         print('This assertion means that there was no Delete button available yet!')
#
#     while element_count < 2:
#         try:
#             form_add = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/button")))
#             if element_count < 2:
#                 element_count += 1
#                 form_add.click()
#                 assert element_count == element_count
#                 print('element count is equal', element_count)
#         except TimeoutException:
#             print('Add/Remove not found')
#     print('Out of the while loop 1!')
#     of_elements = element_count
#     return of_elements


site_open_press_button()

# click_dynamic_load()
# dynamic_page_loaded()
driver.quit()
