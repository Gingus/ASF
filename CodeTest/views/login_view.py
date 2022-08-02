from appium.webdriver.common.mobileby import By
from CodeTest.views.base_view import BaseView
from selenium.common.exceptions import TimeoutException


class LoginView(BaseView):
    """Login Screen"""
    # These might need to go in a dif file!
    CORRECT_USER_INPUT = 'test@qa-experience.com'
    SHORT_USER_INPUT = 'PASSWORD'
    LONG_USER_INPUT = 'PASSWORD76'
    INCORRECT_USER_INPUT = 'QWERTYUIO'
    CORRECT_PASSWORD = 'Password1'

    LOGIN_LINK = 'https://login.dev.qa-experience.com'
    SUCCESS_LINK = 'https://login.dev.qa-experience.com/logged-in'

    USER_LOCATOR = (By.NAME, 'loginUsername')
    PASSWORD_LOCATOR = (By.XPATH, "//input[@name='loginPassword']")
    loginPress = (By.XPATH, "//button[normalize-space()='Login']")

    def find_user(self, user):
        """Find the login link and enter the user name, call with user"""
        self.wait_for(self.By.NAME, 'loginUsername').send_keys(user)
        print('user name found and username', user, 'entered!')

    def find_password(self, password):
        """Find the login link and enter the user name, call with password"""
        self.wait_for(self.By.XPATH, "//input[@name='loginPassword']").send_keys(password)
        print('user name found and username', password, 'entered!')

    def press_login(self):
        """Select login element and press it!"""
        self.wait_for(self.loginPress).click()
        print('Login button found and pressed')

    # Example
    def save_message(self, message):
        """Save the users chosen message"""
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        print('message input send_keys has worked')
        self.wait_for(self.SAVE_BUTTON).click()

    # Example
    def read_message(self):
        """Gets the saved text val from using save_message"""
        try:
            return self.wait_for(self.MESSAGE_LABEL).text
        except TimeoutException:
            return None

    # Example
    def nav_back(self):
        """Taking us back a step to the home page"""
        from CodeTest.views.home_view import LoginView
        self.driver.back()
        return LoginView(self.driver)