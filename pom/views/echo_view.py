from appium.webdriver.common.mobileby import MobileBy
from pom.views.base_view import BaseView
from selenium.common.exceptions import TimeoutException


class EchoView(BaseView):
    """Home screen"""
    MESSAGE_INPUT = (MobileBy.ACCESSIBILITY_ID, 'messageInput')
    SAVE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn')
    MESSAGE_LABEL = (MobileBy.ACCESSIBILITY_ID, 'Hello')

    def save_message(self, message):
        """Save the users chosen message"""
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        self.wait_for(self.SAVE_BUTTON).click()

    def read_message(self):
        """Gets the saved text val from using save_message"""
        try:
            return self.wait_for(self.MESSAGE_LABEL).text
        except TimeoutException:
            return None

    def nav_back(self):
        """Taking us back a step to the home page"""
        from pom.views.home_view import HomeView
        self.driver.back()
        return HomeView(self.driver)
