from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# TODO Open web page 'https://login.dev.qa-experience.com'
# Confirm the login with the presents of,
# Rel XPATH = '//button[Text(),'Add Element']"//label[normalize-space()='Username']"undefined'
# name =

# TODO Username 'test@qa-experience.com'
# Rel XPATH = '//button[Text(),'Add Element']"//input[@name='loginUsername']"undefined'
# name = //button[Text(),'Add Element']"loginUsername"undefined

# TODO Password 'Password1'
# name = //button[Text(),'Add Element']"loginPassword"undefined
# Rel XPATH = '//button[Text(),'Add Element']"//input[@name='loginPassword']"undefined'

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://login.dev.qa-experience.com')
    username = wait.until(EC.presence_of_element_located(
        (By.NAME, 'loginUsername')))

    username.click()

    #  username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
    username.send_keys('test@qa-experience.com')

    password = driver.find_element((By.NAME, 'password'))
    password.send_keys('Password1')

    wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))).click()


    flash = wait.until(EC.presence_of_element_located((By.XPATH, '#flash')))

    assert 'logged out' in flash.text
    print(flash)
    # print(driver.current_url)

finally:
    driver.quit()