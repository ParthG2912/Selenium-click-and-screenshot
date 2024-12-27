from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://www.youtube.com")
    time.sleep(3)

    shorts_btn = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Shorts"]'))
    )
    shorts_btn.click()

    short = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, '0'))
    )
    short.screenshot("short.png")

    input("Press Enter to exit...")
finally:
    driver.quit()
