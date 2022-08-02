from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# https://ui.headspin.io/sessions/80b39568-58a1-11eb-abef-149d997f6e28/waterfall

# When ready to do the challenge!
caps = {
    "headspin:capture": True,
    "headspin:initialScreenSize": {
        "width": 1920,
        "height": 1080
    },
    "browserName": "firefox",
    "browserVersion": "79.0"
}


driver = webdriver.Remote(
    command_executor='https://dev-us-pao-0.headspin.io:9090/v0/417be4d97e4c4fb6935b66a3d4b81b85/wd/hub',
    desired_capabilities=caps)
# driver = webdriver.Firefox()


def site_open_press_button():
    """opens 'the internet' and presses the Add Remove button"""
    cannot_find = "Couldn't find the Add/Remove Elements button"
    try:
        wait = WebDriverWait(driver, 4)
        driver.get('https://the-internet.herokuapp.com')
        form_add_remove = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Add/Remove Elements"))).click()
        form_add_remove_text = wait.until(EC.presence_of_element_located((By.XPATH, "// button[@onclick='addElement()']")))
        wait.until(EC.url_to_be('https://the-internet.herokuapp.com/add_remove_elements/'))
        show_me_path = str(driver.find_elements_by_xpath("//button[@onclick='addElement()']/button"))
        # print(show_me_path_path)
        assert 'Add Element' != show_me_path, 'show_me_path_path matches, this was not expected'
    except NoSuchElementException:
        print(cannot_find)


def check_del_or_press_add():
    """Use a try/Except check for Delete or press Add button until there are two"""
    element_count = int(0)

    try:
        wait = WebDriverWait(driver, 3)
        form_delete = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='elements']/button[1]")))
        wait.until(EC.url_to_be('https://the-internet.herokuapp.com/add_remove_elements/'))

    except TimeoutException:
        see_timeout = str(TimeoutException)
        # print(see_timeout)
        assert 'TimeoutException' in see_timeout, "Assert didn't work!!!"

    while element_count < 2:
        try:
            form_add = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/button")))
            if element_count < 2:
                element_count += 1
                form_add.click()
                show_me_path_count = len(driver.find_elements_by_xpath("//div[@id='elements']//button"))
                assert element_count == show_me_path_count, "element_count & show_me_path_count don't match"
        except TimeoutException:
            print('Add/Remove not found')

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
        except TimeoutException:
            print('Remove not found')
    no_of_elements_two = element_count_two
    return no_of_elements_two


def goto_home():
    """Return to the home page"""
    wait = WebDriverWait(driver, 3)
    driver.get('https://the-internet.herokuapp.com')


site_open_press_button()
showing = int(check_del_or_press_add())
check_del_or_press_remove(showing)
goto_home()
driver.quit()
