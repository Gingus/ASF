from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

class LoginIn():
    """Login screen, login reached, select user field, select password field, error displayed
    login press"""
    # def __init__(self, initial_count=0, max_count=10):
    #     if initial_count < 0:
    #         raise ValueError("Initial cucumber basket count must not be negative")
    #     if max_count < 0:
    #         raise ValueError("Max cucumber basket count must not be negative")
    #
    #     self._count = initial_count
    #     self._max_count = max_count
    def __init__(self):


        def login_reached(self):
            try:
                wait = WebDriverWait(driver, 10)
                driver.get('https://login.dev.qa-experience.com')
                username = wait.until(EC.presence_of_element_located(
                    (By.NAME, 'loginUsername')))
                print('Website located')
                username.click()
            assert presence of username, 'username field was not located so page not loaded'

        def select_user_field(self, username):
            """Add a username when calling"""
            pass

        def select_password_field(self):
            pass

        def error_displayed(self):
            pass

        def login_press(self):
            pass


# TODO Open web page 'https://login.dev.qa-experience.com'


# TODO Username 'test@qa-experience.com'
username.send_keys('test@qa-experience.com')
print('Correct User name entered')
password = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//input[@name='loginPassword']")))
password.click()


print('Password field located')
password.send_keys('Password1')
print('Correct Password entered')


# TODO Password 'Password1'
loginPress = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))).click()
print('Login button located and pressed')

# # TODO Check for confirmation of the login success
# wait = WebDriverWait(driver, 3)
# print(driver.current_url)
# assert driver.current_url == 'https://login.dev.qa-experience.com/logged-in', 'Logged in screen not located'
# print('Login confirmed')

driver.quit()