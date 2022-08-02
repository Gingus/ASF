from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time
# (MobileBy.ACCESSIBILITY_ID, 'messageInput')


def test_echo_box(driver):
    """created the first test for echo box"""
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.TextView[@content-desc != ""]')
        )).send_keys('Hello')
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()
    saved_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Hello'))).text
    assert saved_text == 'Hello', "The saved_text was not equal to 'Hello'"
    driver.back()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    saved_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Hello'))).text
    assert saved_text == 'Hello', "The saved_text was not equal to 'Hello2'"
