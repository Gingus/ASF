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

app = path.join(CUR_DIR, 'ApiDemos.apk')
app_id = 'io.appium.android.apis'

try:
    driver.remove_app(app_id)
    driver.install_app(app)
    driver.activate_app(app_id)
    driver.terminate_app(app_id)

finally:
    driver.quit()

# in apple script to get the app dundle id,
# osasscript -e 'id of app "/path/to/YourApp.app"'

# for an android package id

# apkanalyzer -h manifest application-id /path/to/YourApp.apk
# OR from android studio, find the menu item called 'analize apk'
# type 'analyse apk' in search then look for the file location then double click the Manifest XML and look for,
# package="io.appium.android.apis" near the top!!

# apkanalyzer -h manifest application-id ./ApiDemos.apk, run from the terminal to get the

# Lookup documentation for android app 'Activities' and 'intents'

# to help filter activities for a given app
# aapt list -a ./ApiDemos.apk | grep -E "android:name.+io.appium.android.apis" # for mac/ios
# aapt list -a ./ApiDemos.apk | findstr /i "android:name.*io.appium.android.apis"

# This same info can be found in the android studio > apkanalyzer > manifest XML file!
