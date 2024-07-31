from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from LOCATORS import *


class TestLogout:
    def test_logout(self, driver):
        driver.get(Locators.ACCOUNT_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_TITLE)))
        driver.find_element(By.XPATH, Locators.NAME_FIELD).send_keys(StaticData.LOGIN_NAME)
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(StaticData.LOGIN_PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_TITLE)))
        driver.find_element(By.XPATH, Locators.MAIN_PAGE_TITLE).is_displayed()
        driver.find_element(By.XPATH, Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains(Locators.PROFILE_URL))
        driver.find_element(By.XPATH, Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_BUTTON)))
        assert driver.current_url == Locators.ACCOUNT_URL
