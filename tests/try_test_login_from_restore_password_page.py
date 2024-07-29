import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import Locators

driver = webdriver.Chrome()
driver.get(Locators.FORGOT_PASSWORD_URL)
time.sleep(1)
driver.find_element(By.XPATH,Locators.LOGIN_BUTTON).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_TITLE)))
driver.find_element(By.CSS_SELECTOR, Locators.NAME_FIELD).send_keys(Locators.LOGIN_NAME)
driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_FIELD).send_keys(Locators.LOGIN_PASSWORD)
driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
time.sleep(1)
driver.find_element(By.XPATH, Locators.MAIN_PAGE_TITLE).is_displayed()
driver.find_element(By.XPATH, Locators.ACCOUNT_PAGE_BUTTON).click()
time.sleep(1)
assert Locators.LOGIN_NAME in driver.find_element(By.XPATH, Locators.LOGIN_FILL_IN_ACCOUNT).get_attribute('value')
time.sleep(1)
driver.quit()
