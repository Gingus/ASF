from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from wait_for_elements import *

#When ready to do the challenge!
# caps = {"headspin:capture": True,
#         "headspin:initialScreenSize": {
#             "width": 1920,
#             "height":1080},
#         "browserName": "chrome"}#Copy from heaspin page
#
# driver = webdriver.Remote(command_executor='URL from headspin site', desired_capabilities=caps)
#from wait_for_elements import wait

driver = webdriver.Firefox()

def site_open_press_button():
    """opens 'the internet' and presses the Add Remove button"""
    try:
        wait = WebDriverWait(driver, 5)
        driver.get('https://the-internet.herokuapp.com')
        form_add_remove = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Add/Remove Elements")))
        #print(driver.current_url)
        form_add_remove.click()
        wait.until(EC.url_to_be('https://the-internet.herokuapp.com/add_remove_elements/'))
        print(driver.current_url)

    except NoSuchElementException: # TimeoutException:
        print("Couldn't find the Add/Remove Elements button!")

# To test CSS selector in developer mode goto console and use the following js command
# document.QuerySelector('#Something'), don't forget the '#' when looking for CSS selector
# ALSO
# document.QuerySelector('button(Typr=submit)'), don't forget the '#' when looking for CSS selector

# I can check for the number of 'elements' in TAG_NAME with the following
# els = driver.find_elements(By.TAG_NAME, 'a')
# print(f'There were {len(els)} anchor elements')

# OR

# els = driver.find_elements(By.TAG_NAME, 'foo')# A more targeted approach for 'Delete'
# print(f'There were {len(els)} foo elements')

def check_del_or_press_button():
    """Use a try/Except check for Delete or press Add button"""
    try:
        wait = WebDriverWait(driver, 5)
        form_delete = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#Delete"))) # Caused 'MaxRetryError'

    except TimeoutException:
        #wait = WebDriverWait(driver, 5)
        print('CSS_Selector not found!') # Up to here works
        try:
            form_add = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/button")))
            form_add.click()
            # In the dev tools console:
            # document.querySelectorAll(id='elements') in find
            # OR for XPATH
            # $x("xpath in here"), example below!
            # $x("/html/body/div[2]/div/div/button")
            # Note: In thr inspector code on the right, right click > copy > xpath
        except TimeoutException:
            print("Well that one didn't work!")
            driver.quit()
            pass
        #pass
#         form_add = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Add Element")))
#         form_add.click()
#         print("No Delete button was present so 'Add Element' was pressed")
#         /html/body/div[2]/div/div/button = xpath to the 'Add Element Button

site_open_press_button()
check_del_or_press_button()
#driver.quit()

