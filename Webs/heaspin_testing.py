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
        # print(driver.current_url)
        form_add_remove.click()
        wait.until(EC.url_to_be('https://the-internet.herokuapp.com/add_remove_elements/'))
        print(driver.current_url)

    except NoSuchElementException:  # TimeoutException:
        print("Couldn't find the Add/Remove Elements button!")


def check_del_or_press_button():
    """Use a try/Except check for Delete or press Add button"""
    element_count = int()

    try:
        wait = WebDriverWait(driver, 3)
        form_delete = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#Delete")))
        # driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
        #
        # wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Logout'))).click()
        #
        # flash = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#flash')))
        #
        # assert 'logged out' in flash.text
        # print(flash)
        # print(driver.current_url)

    except TimeoutException:
        wait = WebDriverWait(driver, 3)
        print('CSS_Selector not found!') # Up to here works
        assert TimeoutException
        print('This assertion means that there was no Delete button available yet!')

        # def increase():

        # def decrease()

        while element_count <= 2:
            try:
                form_add = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/button")))
                form_add.click()
                # print(element_count)
                print('element count is equal', element_count)
                # if element_count <= 2:
                element_count += 1
                assert element_count == element_count
                # else:
                #     if element_count == 3:
                #         element_count -= 1

            except TimeoutException:
                assert element_count == 0
                print('element count is equal', element_count)
                # driver.quit()
        print('Out of the while loop!')

        while element_count >= 0:
            try:
                form_add = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/button")))
                form_add.click()
                # print(element_count)
                print('element count is equal', element_count)
                # if element_count <= 2:
                element_count -= 1
                assert element_count == element_count
                # else:
                #     if element_count == 3:
                #         element_count -= 1

            except TimeoutException:
                assert element_count == 0
                print('element count is equal', element_count)
                # driver.quit()

        print('Dropped out of the second while loop!')


site_open_press_button()
check_del_or_press_button()
driver.quit()

# finally:
driver.quit()
