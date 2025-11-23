import pytest
class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(45)
        self._driver.maximize_window()

class SecondPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()