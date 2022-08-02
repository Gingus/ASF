from appium import webdriver
from os import path


CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'
CAPS = {
    'platform': 'Android',
    'deviceName': 'pixel_4',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    print(driver.execute_script("mobile: deviceInfo"))
finally:
    driver.quit()

# in apple script to get the app dundle id,
# osasscript -e 'id of app "/path/to/YourApp.app"'

# for an android package id
# apkanalyzer -h manifest application-id /path/to/YourApp.apk
# OR from android studio, find the menu item called 'analize apk'
