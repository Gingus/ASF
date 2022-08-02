from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseView(object):
    """Base for all other pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for(self, locator):
        """Abstracts the wait until for all pages"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        """So we don't have to remember '*' before locator in driver.call"""
        return self.driver.find_element(*locator)

