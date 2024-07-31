from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from LOCATORS import *


class TestProfilePage:
    def test_redirect_account_page_button(self, driver):
        driver.get(Locators.BASE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locators.LOGIN_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_TITLE)))
        driver.find_element(By.XPATH, Locators.NAME_FIELD).send_keys(StaticData.LOGIN_NAME)
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(StaticData.LOGIN_PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.MAIN_PAGE_TITLE)))
        driver.find_element(By.XPATH, Locators.MAIN_PAGE_TITLE).is_displayed()
        driver.find_element(By.XPATH, Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGOUT_BUTTON)))
        assert driver.current_url == Locators.PROFILE_URL
