import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import LOCATORS


def test_redirect_account_page_button(driver):
    driver.get(LOCATORS.BASE_URL)
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
    assert driver.current_url == LOCATORS.PROFILE_URL
    time.sleep(1)
    driver.quit()
