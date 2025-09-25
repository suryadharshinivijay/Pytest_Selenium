import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    global driver
    driver = webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(10)
    yield driver
    driver.close()