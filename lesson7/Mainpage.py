import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(45)
        self._driver.maximize_window()
        set_delay(seconds)
        click_number(number)
        click_operator(operator)
        click_equals()
        get_result()


class SecondPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

class LoginPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com")

        username = driver.find_element(By.CSS_SELECTOR, "#user-name")
        username.send_keys("standard_user")
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")