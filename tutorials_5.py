from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
print(driver.get_window_size())
time.sleep(3)

driver.maximize_window()


input_box = driver.find_element(By.ID, "email")
input_box.clear()
input_box.send_keys("Test@gmail.com")

input_box = driver.find_element(By.ID, "pass")
input_box.clear()
input_box.send_keys("Password")

login_button = driver.find_element(By.NAME, "login")
login_button.click()
time.sleep(5)
