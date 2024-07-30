from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import LOCATORS


def test_correct_data_registration(create_random_name, create_random_password, create_random_email, driver):
    driver.get(LOCATORS.REGISTER_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_NAME).send_keys(create_random_name)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_EMAIL).send_keys(create_random_email)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_PASSWORD).send_keys(create_random_password)
    driver.find_element(By.XPATH, LOCATORS.REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.LOGIN_TITLE)))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.NAME_FIELD).send_keys(create_random_email)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.PASSWORD_FIELD).send_keys(create_random_password)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.MAIN_PAGE_TITLE).is_displayed()
    driver.find_element(By.XPATH, LOCATORS.ACCOUNT_PAGE_BUTTON).click()
    time.sleep(1)
    assert create_random_email.lower() in driver.find_element(By.XPATH, LOCATORS.LOGIN_FILL_IN_ACCOUNT).get_attribute(
        'value')
    time.sleep(1)
    driver.quit()


def test_incorrect_email_registration(create_random_name, create_incorrect_random_email, create_random_password, driver):
    driver.get(LOCATORS.REGISTER_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_NAME).send_keys(create_random_name)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_EMAIL).send_keys(create_incorrect_random_email)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_PASSWORD).send_keys(create_random_password)
    driver.find_element(By.XPATH, LOCATORS.REGISTER_BUTTON).click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, LOCATORS.ALERT_POPUP).is_displayed()
    time.sleep(1)
    driver.quit()


def test_incorrect_name_registration(create_random_email, create_random_password, driver):
    driver.get(LOCATORS.REGISTER_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_NAME).send_keys('')
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_EMAIL).send_keys(create_random_email)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_PASSWORD).send_keys(create_random_password)
    driver.find_element(By.XPATH, LOCATORS.REGISTER_BUTTON).click()
    time.sleep(1)
    assert driver.current_url is not LOCATORS.ACCOUNT_URL
    time.sleep(1)
    driver.quit()


def test_incorrect_password_registration(create_random_name, create_random_email, create_incorrect_random_password, driver):
    driver.get(LOCATORS.REGISTER_URL)
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_NAME).send_keys(create_random_name)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_EMAIL).send_keys(create_random_email)
    driver.find_element(By.XPATH, LOCATORS.REG_FIELD_PASSWORD).send_keys(create_incorrect_random_password)
    driver.find_element(By.XPATH, LOCATORS.REGISTER_BUTTON).click()
    assert driver.find_element(By.XPATH, LOCATORS.ALERT_INCORRECT_PASSWORD).is_displayed()
    time.sleep(1)
    driver.quit()
