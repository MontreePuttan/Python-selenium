#How to select dropdown value

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
print(driver.get_window_size())
time.sleep(3)

driver.maximize_window()

create_account_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="open-registration-form-button"]')
create_account_button.click()


#day_element = driver.find_element(By.ID, 'day')
#select = Select(day_element)
#select.select_by_index(2)
