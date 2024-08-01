from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.by import By
from LOCATORS import *


def test_correct_data_registration(create_random_name, create_random_password, create_random_email, driver):
    driver.get(Locators.REGISTER_URL)
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.REG_FIELD_NAME)))
    driver.find_element(By.XPATH, Locators.REG_FIELD_NAME).send_keys(create_random_name)
    driver.find_element(By.XPATH, Locators.REG_FIELD_EMAIL).send_keys(create_random_email)
    driver.find_element(By.XPATH, Locators.REG_FIELD_PASSWORD).send_keys(create_random_password)
    driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_TITLE)))
    driver.find_element(By.XPATH, Locators.NAME_FIELD).send_keys(create_random_email)
    driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(create_random_password)
    driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_TITLE)))
    driver.find_element(By.XPATH, Locators.MAIN_PAGE_TITLE).is_displayed()
    driver.find_element(By.XPATH, Locators.ACCOUNT_PAGE_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_FILL_IN_ACCOUNT)))
    assert create_random_email.lower() in driver.find_element(By.XPATH, Locators.LOGIN_FILL_IN_ACCOUNT).get_attribute(
        'value')


def test_incorrect_email_registration(create_random_name, create_incorrect_random_email, create_random_password,
                                      driver):
    driver.get(Locators.REGISTER_URL)
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.REG_FIELD_NAME)))
    driver.find_element(By.XPATH, Locators.REG_FIELD_NAME).send_keys(create_random_name)
    driver.find_element(By.XPATH, Locators.REG_FIELD_EMAIL).send_keys(create_incorrect_random_email)
    driver.find_element(By.XPATH, Locators.REG_FIELD_PASSWORD).send_keys(create_random_password)
    driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, Locators.ALERT_POPUP)))
    assert driver.find_element(By.XPATH, Locators.ALERT_POPUP).is_displayed()


class TestRegister:
    def test_incorrect_name_registration(self, create_random_email, create_random_password, driver):
        driver.get(Locators.REGISTER_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.REG_FIELD_NAME)))
        driver.find_element(By.XPATH, Locators.REG_FIELD_NAME).send_keys('')
        driver.find_element(By.XPATH, Locators.REG_FIELD_EMAIL).send_keys(create_random_email)
        driver.find_element(By.XPATH, Locators.REG_FIELD_PASSWORD).send_keys(create_random_password)
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()
        time.sleep(1)
        assert driver.current_url is not Locators.ACCOUNT_URL

    def test_incorrect_password_registration(self, create_random_name, create_random_email,
                                             create_incorrect_random_password,
                                             driver):
        driver.get(Locators.REGISTER_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.REG_FIELD_NAME)))
        driver.find_element(By.XPATH, Locators.REG_FIELD_NAME).send_keys(create_random_name)
        driver.find_element(By.XPATH, Locators.REG_FIELD_EMAIL).send_keys(create_random_email)
        driver.find_element(By.XPATH, Locators.REG_FIELD_PASSWORD).send_keys(create_incorrect_random_password)
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_BUTTON)))
        assert driver.find_element(By.XPATH, Locators.ALERT_INCORRECT_PASSWORD).is_displayed()
