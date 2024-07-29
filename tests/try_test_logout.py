import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import Locators

driver = webdriver.Chrome()

driver.get(Locators.ACCOUNT_URL)
time.sleep(1)
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_TITLE)))
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, Locators.NAME_FIELD).send_keys(Locators.LOGIN_NAME)
driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_FIELD).send_keys(Locators.LOGIN_PASSWORD)
driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
time.sleep(1)
driver.find_element(By.XPATH, Locators.MAIN_PAGE_TITLE).is_displayed()
driver.find_element(By.XPATH, Locators.ACCOUNT_PAGE_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.url_contains(Locators.PROFILE_URL))
driver.find_element(By.XPATH, Locators.LOGOUT_BUTTON).click()
time.sleep(1)
assert driver.current_url == Locators.LOGIN_URL
time.sleep(1)
driver.quit()
