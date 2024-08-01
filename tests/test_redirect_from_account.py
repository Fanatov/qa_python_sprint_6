from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from LOCATORS import *


class TestRedirect:
    def test_redirect_builder_page_button(self, driver):
        driver.get(Locators.ACCOUNT_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.PAGE_HEADER)))
        driver.find_element(By.XPATH, Locators.NAME_FIELD).send_keys(StaticData.LOGIN_NAME)
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(StaticData.LOGIN_PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.BUILDER_BUTTON)))
        driver.find_element(By.XPATH, Locators.BUILDER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.INGRIDIENTS_SECTION)))
        assert driver.find_element(By.XPATH, Locators.INGRIDIENTS_SECTION).is_displayed()

    def test_redirect_logo_page_click(self, driver):
        driver.get(Locators.ACCOUNT_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.PAGE_HEADER)))
        driver.find_element(By.XPATH, Locators.NAME_FIELD).send_keys(StaticData.LOGIN_NAME)
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(StaticData.LOGIN_PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGO_MAIN_PAGE)))
        driver.find_element(By.XPATH, Locators.LOGO_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.INGRIDIENTS_SECTION)))
        assert driver.find_element(By.XPATH, Locators.INGRIDIENTS_SECTION).is_displayed()
