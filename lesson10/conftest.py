import pytest
from selenium import webdriver

@allure.feature("")
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()