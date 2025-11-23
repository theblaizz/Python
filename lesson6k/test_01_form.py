import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_fill_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    email.send_keys("test@skypro.com")

    phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
    phone.send_keys("+7985899998787")

    city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
    country.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
    company.send_keys("SkyPro")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    assert "data-types" in driver.current_url