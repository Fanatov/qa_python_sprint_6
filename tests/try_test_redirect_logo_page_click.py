import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import Locators

driver = webdriver.Chrome()
driver.get(Locators.FEED_URL)
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.PAGE_HEADER)))
time.sleep(1)
driver.find_element(By.XPATH, Locators.LOGO_MAIN_PAGE).click()
assert driver.find_element(By.XPATH, Locators.INGRIDIENTS_SECTION).is_displayed()
time.sleep(1)
driver.quit()
