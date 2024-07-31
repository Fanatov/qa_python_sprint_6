import random
import string
import pytest
from selenium import webdriver



@pytest.fixture
def create_random_password():
    password = ''.join(random.choices(string.ascii_letters, k=8))
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    result_password = f'{password}{random_digits}'
    return result_password


@pytest.fixture
def create_random_email():
    first_name = ''.join(random.choices(string.ascii_letters, k=8))
    last_name = ''.join(random.choices(string.ascii_letters, k=8))
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    email = f'{first_name}{last_name}12{random_digits}@yandex.ru'
    return email


@pytest.fixture()
def create_random_name():
    name = ''.join(random.choices(string.ascii_letters, k=5))
    random_digits = str(random.randint(1, 1999))
    result_name = name + random_digits
    return result_name


@pytest.fixture
def create_incorrect_random_email():
    first_name = ''.join(random.choices(string.ascii_letters, k=8))
    last_name = ''.join(random.choices(string.ascii_letters, k=8))
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    incorrect_email = f'{first_name}{last_name}12{random_digits}@yandex'
    return incorrect_email


@pytest.fixture
def create_incorrect_random_password():
    password = ''.join(random.choices(string.ascii_letters, k=2))
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(2)])
    result_incorrect_password = f'{password}{random_digits}'
    return result_incorrect_password


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
