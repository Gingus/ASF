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
    cannot_find = "Couldn't find the Add/Remove Elements button"
    try:
        wait = WebDriverWait(driver, 3)
        driver.get('https://the-internet.herokuapp.com')
        form_add_remove = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Add/Remove Elements"))).click()
        # form_add_remove.click()
        form_add_remove_text = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@onclick='addElement()']")))
        wait.until(EC.url_to_be('https://the-internet.herokuapp.com/add_remove_elements/'))
    except NoSuchElementException:
        print(cannot_find)
    assert form_add_remove_text.text == 'Add Element', 'Add Element was not found'
    # print(form_add_remove_text.text, 'found and asserted!')


def check_del_or_press_add():
    """Use a try/Except check for Delete or press Add button until there are two"""
    element_count = int(0)

    try:
        wait = WebDriverWait(driver, 3)
        form_delete = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='elements']/button[1]")))
        wait.until(EC.url_to_be('https://the-internet.herokuapp.com/add_remove_elements/'))

    except TimeoutException:
        # print('Timeout Caught')
        see_timeout = str(TimeoutException)
        # print(see_timeout)
        assert 'TimeoutException' in see_timeout, "Assert didn't work!!!"
        # print("Exception asserted so no button one was present and so one is created")

    while element_count < 2:
        # assert 'Delete' not in flash.text
        try:
            form_add = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/button")))
            if element_count < 2:
                element_count += 1
                form_add.click()
                show_me_path_count = len(driver.find_elements_by_xpath("//div[@id='elements']//button"))
                assert element_count == show_me_path_count, "element_count & show_me_path_count don't match"
                print('show me path count is =', show_me_path_count)
                # For this assertion, need to count the number of buttons in the xpath and assign it to a variable
                # print('element count is equal', element_count)
        except TimeoutException:
            print('Add/Remove not found')
    print('Out of the while loop 1!')
    of_elements = element_count
    return of_elements


def check_del_or_press_remove(of_elements):
    """Use a try/Except check for Deleting the added buttons until there are none left"""
    element_count_two = int(of_elements)
    while element_count_two > 0:
        try:
            wait = WebDriverWait(driver, 1)
            form_remove = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/button[1]")))
            if element_count_two > 0:
                element_count_two -= 1
                form_remove.click()
                show_me_path_count = len(driver.find_elements_by_xpath("//div[@id='elements']//button"))
                assert element_count_two == show_me_path_count, "element_count & show_me_path_count don't match"
                # print('element two is equal', element_count_two)
        except TimeoutException:
            print('Remove not found')
    # print('No Delete Buttons are left!')
    print('Out of the 2nd while loop!')
    no_of_elements_two = element_count_two
    return no_of_elements_two


site_open_press_button()
showing = int(check_del_or_press_add())
# print(showing)
check_del_or_press_remove(showing)
# print(showing)
# print(showing_two)
driver.quit()

