import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import Locators

driver = webdriver.Chrome()
driver.get(Locators.BASE_URL)
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.INGRIDIENTS_SECTION)))
time.sleep(1)
driver.find_element(By.XPATH, Locators.SAUCES_BUTTON).click()
time.sleep(1)
driver.find_element(By.XPATH, Locators.BUNS_BUTTON).click()
assert driver.find_element(By.XPATH, Locators.SELECTED_INGRIDIENT).text == "Булки"
time.sleep(1)
driver.quit()
