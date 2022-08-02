from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
try:
    driver.get('https://the-internet.herokuapp.com')
    driver.find_element(By.LINK_TEXT, 'Form Authentication')
    els = driver.find_elements(By.TAG_NAME, 'a')
    print(f'Yhere were {len(els)} anchor elements')

    els = driver.find_elements(By.TAG_NAME, 'foo')
    print(f'Yhere were {len(els)} foo elements')

finally:
    driver.quit()

