from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#When ready to do the challenge!
caps = {"headspin:capture": True,
        "headspin:initialScreenSize": {
            "width": 1920,
            "height":1080},
        "browserName": "chrome"}#Copy from heaspin page

#driver = webdriver.Firefox()

driver = webdriver.Remote(command_executor='URL from headspin site', desired_capabilities=caps)
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')))
    form_auth_link.click()

    username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
    username.send_keys('tomsmith')
    password = driver.find_element(By.CSS_SELECTOR,'#password')
    password.send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Logout'))).click()

    flash = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#flash')))

    assert 'logged out' in flash.text
    #print(driver.current_url)

finally:
    driver.quit()

