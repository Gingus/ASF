from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APPIUM = 'http://localhost:4723'
CAPS = {
    'platform': 'Android',
    'deviceName': 'pixel4',
    'automationName': 'UiAutomator2',
    'browserName': 'Chrome',
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')))
    form_auth_link.click()

    username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
    username.send_keys('tomsmith')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Logout'))).click()

    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/login'))
    flash = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#flash')))

    # print(flash.text)
    assert 'logged out' in flash.text
    print(flash)
    #print(driver.current_url)

finally:
    driver.quit()

# appium --allow-insecure=chromedriver_autodownload
# Use this to start appium when automating chrome on android!!!

# chromedriverExecutableDir 'path/to/a/dir'
#  chromedriverChomeMappingFile

# Ask dev to turn on WebView.setWebContentsDebuggingEnable(true);

# context commands
# ctxs = driver.contexts, Returns a list of available context. "NATIVE_APP" plus any webview context ids
# ctx = driver.context, Returns the currently-active context

