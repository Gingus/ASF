firstly my webdriver wait time is 30

wait = WebDriverWait(driver, 30)

and then the code

have a look, and compare if its same with you


#Switch to Webview
wait.until(webview_active())


text_1 = driver.find_element(By.XPATH, "//h1[text()='Please navigate to a webpage']").text
print(text_1)

#Launch the URL

driver.get("http://the-internet.herokuapp.com")


# Click Form Authentication
form_auth_link = wait.until(EC.presence_of_element_located(
(By.LINK_TEXT, 'Form Authentication')
))
form_auth_link.click()

# Enter username
username = wait.until(EC.presence_of_element_located(
(By.CSS_SELECTOR, '#username')))

username.send_keys('tomsmith')

# Enter Password
password = driver.find_element(By.CSS_SELECTOR, '#password')

password.send_keys('SuperSecretPassword!')

# Click Login
Login = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
Login.click()

# Click Logout
wait.until(EC.presence_of_element_located(
(By.LINK_TEXT, 'Logout')
)).click()

flash = wait.until(EC.presence_of_element_located(
(By.CSS_SELECTOR, '#flash')
))

assert 'logged out' in flash.text

# Switch back to Native context
driver.switch_to.context('NATIVE_APP')

# To Clear the URL in the text field

btn_clear = wait.until(EC.presence_of_element_located(
(MobileBy.ACCESSIBILITY_ID, 'clearBtn')
))
btn_clear.click()