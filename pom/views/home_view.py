from appium.webdriver.common.mobileby import MobileBy
from pom.views.base_view import BaseView
from pom.views.echo_view import EchoView


class HomeView(BaseView):
    """Home screen"""
    ECHO_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Echo Box')

    def nav_to_echo_box(self):
        """Navigate to the echo box selection"""
        self.wait_for(self.ECHO_ITEM).click(), but
        return EchoView(self.driver)
