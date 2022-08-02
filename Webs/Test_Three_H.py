from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

# When ready to do the challenge!
# caps = {"headspin:capture": True,
#         "headspin:initialScreenSize": {
#             "width": 1920,
#             "height":1080},
#         "browserName": "chrome"}#Copy from headspin page

driver = webdriver.Firefox()

def frames_link():
f_link = wait.until(EC.presence_of_element_located(
(By.LINK_TEXT, 'Frames')
))
f_link.click()

frames_link()

def frames_win():
i_frame = wait.until(EC.presence_of_element_located(
(By.LINK_TEXT, 'iFrame')
))
i_frame.click()
frames_win()

header_frame_title = driver.find_element(By.XPATH, "//h3[contains(text(),'An iFrame containing the TinyMCE WYSIWYG Editor')]").text
assert 'An iFrame containing the TinyMCE WYSIWYG Editor' in header_frame_title
print('Assertion iFrame - Pass')

file_btn = wait.until(EC.presence_of_element_located(
(By.XPATH, "//span[contains(text(),'File')]")
))
file_btn.click()


new_document = driver.find_element(By.XPATH, "//div[@class='tox-collection__item-label']")
new_document.click()

time.sleep(2)
driver.switch_to.frame("mce_0_ifr")
time.sleep(2)
text_area = driver.find_element(By.XPATH, "//body[@id='tinymce']")
text_area.clear()
time.sleep(2)
text_area.send_keys("Hello from automation!")

actual_text = driver.find_element(By.XPATH,"//body[@id='tinymce']").text
print('Text captured : ' ,actual_text)
assert actual_text == "Hello from automation!"
print('The text matches ')

time.sleep(3)
driver.switch_to.default_content()

def go_back_browser():
driver.back()

go_back_browser()