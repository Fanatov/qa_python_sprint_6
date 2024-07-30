import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import LOCATORS


def test_redirect_ingridients_buns(driver):
    driver.get(LOCATORS.BASE_URL)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.INGRIDIENTS_SECTION)))
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.SAUCES_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.BUNS_BUTTON).click()
    assert driver.find_element(By.XPATH, LOCATORS.SELECTED_INGRIDIENT).text == "Булки"
    time.sleep(1)
    driver.quit()


def test_redirect_ingridients_fillings(driver):
    driver.get(LOCATORS.BASE_URL)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.INGRIDIENTS_SECTION)))
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.FILLINGS_BUTTON).click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, LOCATORS.SELECTED_INGRIDIENT).text == "Начинки"
    time.sleep(1)
    driver.quit()


def test_redirect_ingridients_sauces(driver):
    driver.get(LOCATORS.BASE_URL)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOCATORS.INGRIDIENTS_SECTION)))
    time.sleep(1)
    driver.find_element(By.XPATH, LOCATORS.SAUCES_BUTTON).click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, LOCATORS.SELECTED_INGRIDIENT).text == "Соусы"
    time.sleep(1)
    driver.quit()
