from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Firefox()
# tool = ''
LOOPCALCULATOR = "//a[contains(text(),'Loop Calculator')]"
TESTSET = "//a[contains(text(),'Test Set Firmware Update')]"
EXERT = "//a[contains(text(),'XPERT Address Tool')]"
DILSWITCH = "//a[contains(text(),'DIL Switch Addressing')]"
DATINGDETECTOR = "//a[contains(text(),'Dating a Detector')]"
GUIDES = "//a[contains(text(),'Guides')]"


# Open web page
homePage = 'https://www.apollo-fire.co.uk/' # Home page
training = 'https://www.apollo-fire.co.uk/training-support/'  # Tools page
startingPoint = training
wait = WebDriverWait(driver, 10)
driver.get(startingPoint) # opens the tool page

cookieAcceptClose = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, '.onetrust-lg')))
cookieAcceptClose.click() # Cookies accepted

trainingPage = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//h1[normalize-space()='Welcome to Training & Support']")))

driver = webdriver.Firefox(executable_path='...')
driver.get(startingPoint)
driver.execute_script("document.body.style.zoom='75%'")

gotoToolPage = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//a[contains(text(),'Tools')]"))).click()
# assert with the presents of '//h1[normalize-space()="Welcome to Training & Support"]'
print('Tools page reached')


gotoLoopCalculator = wait.until(EC.presence_of_element_located(
    (By.XPATH, LOOPCALCULATOR))).click()
print('Loop Calculator page reached') # Use assert statement here
WebDriverWait(driver, 1.5)
# driver.back()
driver.execute_script("window.history.go(-1)")

print(' page reached')
# print('Closed Cookie Notice')
#
# WebDriverWait(driver, 10)
# print('Waited 10 seconds!')
#

# darkHeaderPresent = wait.until(EC.presence_of_element_located(
#     (By.XPATH, 	"//ul[@class='headerButtons']")))
# print("Dark header bar present!")
# WebDriverWait(driver, 5)
# menuButtonPress = wait.until(EC.presence_of_element_located(
#     (By.XPATH, "//button[@class='button icon nav']"))).click()


# try:
#     selectingTrainingTab = wait.until(EC.presence_of_element_located(
#     (By.XPATH, "/ul[@class='headerNavList level1']/li[3]/a[1]"))).click()
# except ElementNotInteractableException:
#     print("Top menu bar was not accessible!")
#
# try:
#     selectedTrainingTab = wait.until(EC.presence_of_element_located(
#         (By.XPATH, "html[1]/body[1]/header[1]/nav[1]/ul[1]/li[3]/a[1]"))).click()
# except:
#     pass
# driver.quit()

# stickyMenuButtonPress.click()

# class="headerNavLink" tabindex="0" data-href="/training-support/"
# //button[Text(),'Add Element']"//span[normalize-space()='Training & Support']"undefined
# //button[Text(),'Add Element']".headerNavLink[href='/training-support/']"undefined
# //button[Text(),'Add Element']"//body/header[@class='header stuck']/
# nav[@class='headerNav']/ul[@class='headerNavList level1']/li[3]/a[1]"undefined
# /html[1]/body[1]/header[1]/nav[1]/ul[1]/li[3]/a[1]/span[1]
# //span[contains(text(),'Training & Support')]