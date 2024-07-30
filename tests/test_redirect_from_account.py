import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import LOCATORS


def test_redirect_builder_page_button(driver):
    driver.get(LOCATORS.ACCOUNT_URL)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.PAGE_HEADER)))
    time.sleep(1)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.NAME_FIELD).send_keys(LOCATORS.LOGIN_NAME)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.PASSWORD_FIELD).send_keys(LOCATORS.LOGIN_PASSWORD)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.ACCOUNT_PAGE_BUTTON).click()
    driver.find_element(By.XPATH, LOCATORS.BUILDER_BUTTON).click()
    assert driver.find_element(By.XPATH, LOCATORS.INGRIDIENTS_SECTION).is_displayed()
    time.sleep(1)
    driver.quit()


def test_redirect_logo_page_click(driver):
    driver.get(LOCATORS.ACCOUNT_URL)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.PAGE_HEADER)))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.NAME_FIELD).send_keys(LOCATORS.LOGIN_NAME)
    driver.find_element(By.CSS_SELECTOR, LOCATORS.PASSWORD_FIELD).send_keys(LOCATORS.LOGIN_PASSWORD)
    driver.find_element(By.XPATH, LOCATORS.LOGIN_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.ACCOUNT_PAGE_BUTTON).click()
    driver.find_element(By.XPATH, LOCATORS.LOGO_MAIN_PAGE).click()
    assert driver.find_element(By.XPATH, LOCATORS.INGRIDIENTS_SECTION).is_displayed()
    time.sleep(1)
    driver.quit()
