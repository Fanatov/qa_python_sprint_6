import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import LOCATORS


def test_login_form_account_page(driver):
    driver.get(LOCATORS.BASE_URL)
    time.sleep(1)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.LOGIN_BUTTON)))
    driver.find_element(By.XPATH, LOCATORS.LOGIN_INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.LOGIN_TITLE)))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.NAME_FIELD).send_keys(LOCATORS.LOGIN_NAME)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.PASSWORD_FIELD).send_keys(LOCATORS.LOGIN_PASSWORD)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.MAIN_PAGE_TITLE).is_displayed()
    driver.find_element(By.XPATH, LOCATORS.ACCOUNT_PAGE_BUTTON).click()
    time.sleep(1)
    assert LOCATORS.LOGIN_NAME in driver.find_element(By.XPATH, LOCATORS.LOGIN_FILL_IN_ACCOUNT).get_attribute('value')
    time.sleep(1)
    driver.quit()


def test_login_from_main_page(driver):
    driver.get(LOCATORS.BASE_URL)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.LOGIN_BUTTON)))
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.LOGIN_TITLE)))
    driver.find_element(By.CSS_SELECTOR, LOCATORS.NAME_FIELD).send_keys(LOCATORS.LOGIN_NAME)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.PASSWORD_FIELD).send_keys(LOCATORS.LOGIN_PASSWORD)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.MAIN_PAGE_TITLE).is_displayed()
    driver.find_element(By.XPATH, LOCATORS.ACCOUNT_PAGE_BUTTON).click()
    time.sleep(1)
    assert LOCATORS.LOGIN_NAME in driver.find_element(By.XPATH, LOCATORS.LOGIN_FILL_IN_ACCOUNT).get_attribute('value')
    time.sleep(1)
    driver.quit()


def test_login_from_register_page(driver):
    driver.get(LOCATORS.REGISTER_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.LOGIN_TITLE)))
    driver.find_element(By.CSS_SELECTOR, LOCATORS.NAME_FIELD).send_keys(LOCATORS.LOGIN_NAME)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.PASSWORD_FIELD).send_keys(LOCATORS.LOGIN_PASSWORD)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.MAIN_PAGE_TITLE).is_displayed()
    driver.find_element(By.XPATH, LOCATORS.ACCOUNT_PAGE_BUTTON).click()
    time.sleep(1)
    assert LOCATORS.LOGIN_NAME in driver.find_element(By.XPATH, LOCATORS.LOGIN_FILL_IN_ACCOUNT).get_attribute('value')
    time.sleep(1)
    driver.quit()


def test_login_from_restore_password_page(driver):
    driver.get(LOCATORS.FORGOT_PASSWORD_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.LOGIN_TITLE)))
    driver.find_element(By.CSS_SELECTOR, LOCATORS.NAME_FIELD).send_keys(LOCATORS.LOGIN_NAME)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.PASSWORD_FIELD).send_keys(LOCATORS.LOGIN_PASSWORD)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.MAIN_PAGE_TITLE).is_displayed()
    driver.find_element(By.XPATH, LOCATORS.ACCOUNT_PAGE_BUTTON).click()
    time.sleep(1)
    assert LOCATORS.LOGIN_NAME in driver.find_element(By.XPATH, LOCATORS.LOGIN_FILL_IN_ACCOUNT).get_attribute('value')
    time.sleep(1)
    driver.quit()
