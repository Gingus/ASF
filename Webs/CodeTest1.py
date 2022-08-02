from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# TODO Open web page 'https://login.dev.qa-experience.com'
wait = WebDriverWait(driver, 10)
driver.get('https://login.dev.qa-experience.com')
username = wait.until(EC.presence_of_element_located(
    (By.NAME, 'loginUsername')))
print('Website located')
username.click()

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

# TODO Check for confirmation of the login success
wait = WebDriverWait(driver, 3)
print(driver.current_url)
assert driver.current_url == 'https://login.dev.qa-experience.com/logged-in', 'Logged in screen not located'
print('Login confirmed')

driver.quit()