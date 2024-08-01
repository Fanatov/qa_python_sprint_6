from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from LOCATORS import *


class TestBuilder:
    def test_redirect_ingridients_buns(self,driver):
        driver.get(Locators.BASE_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.INGRIDIENTS_SECTION)))
        driver.find_element(By.XPATH, Locators.SAUCES_BUTTON).click()
        driver.find_element(By.XPATH, Locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.SELECTED_INGRIDIENT)))
        assert driver.find_element(By.XPATH, Locators.SELECTED_INGRIDIENT).text == StaticData.BUNS


    def test_redirect_ingridients_fillings(self,driver):
        driver.get(Locators.BASE_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.INGRIDIENTS_SECTION)))
        driver.find_element(By.XPATH, Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.SELECTED_INGRIDIENT)))
        assert driver.find_element(By.XPATH, Locators.SELECTED_INGRIDIENT).text == StaticData.FILLINGS


    def test_redirect_ingridients_sauces(self,driver):
        driver.get(Locators.BASE_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, Locators.INGRIDIENTS_SECTION)))
        driver.find_element(By.XPATH, Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.SELECTED_INGRIDIENT)))
        assert driver.find_element(By.XPATH, Locators.SELECTED_INGRIDIENT).text == StaticData.SAUCES
