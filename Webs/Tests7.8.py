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
        form_add_remove_text = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[@onclick='addElement()']")))
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
            form_add = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add Element']")))
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
            # move = driver.switch_to((By.XPATH, "//div[@id='elements']"))
            form_remove = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='elements']//button[1]")))
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


def site_open_press_button_two():
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
        start_button_pressed = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Start']")))
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


def site_open_press_button_three():
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


site_open_press_button()
showing = int(check_del_or_press_add())
check_del_or_press_remove(showing)
goto_home()

site_open_press_button_two()
second_selection_press()
the_start_button()
checking()
goto_home()

site_open_press_button_three()
select_iframe_button()
check4_iframe_page()
select_file_add()
sel_new_doc()
switch_to_iframe()
show_me()
goto_home()
driver.quit()


