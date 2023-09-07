from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://th.trovit.com/baan/")
time.sleep(3)

keyword = "เชียงใหม่"
#input_box = driver.find_element("what_d") 
input_box = driver.find_element(By.ID, "what_d")
input_box.clear()
input_box.send_keys(keyword)

click_search = driver.find_element(By.TAG_NAME, "button")
click_search.click()
time.sleep(15)
