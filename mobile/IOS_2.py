if you ask me.. where in the beginning.. then it's here
APPIUM = 'https://dev-us-pao-0.headspin.io:7044/v0/8075f539149847748d914adcc386fd3f/wd/hub'

CAPS = {
'platformName': 'iOS',
'automationName': 'XCUITest',
'bundleId': 'com.apple.Maps',
'deviceName': 'iPhone 12',
'platformVersion': '14.1',
'udid': '00008101-0011756C3E20001E',
'headspin:capture': True,
}

driver = webdriver.Remote(APPIUM, CAPS)
#driver.terminate_app('com.apple.Maps')
try:
wait = WebDriverWait(driver, 30)


def search_place():
wait = WebDriverWait(driver, 30)
#Enter into text field
search_text = wait.until(EC.presence_of_element_located(
(By.ID,'Search for a place or address')
))
# search_text = driver.find_element(By.ID,'Search for a place or address')
search_text.send_keys('Vancouver, BC')

so before every run, it will teminate the maps if they are open