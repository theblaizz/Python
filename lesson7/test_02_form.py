import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Mainpage import SecondPage
from Mainpage import LoginPage
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_saucedemo_shopping(driver):
    driver.get("https://www.saucedemo.com")

    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()

    backpack_button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    backpack_button.click()

    tshirt_button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    tshirt_button.click()

    onesie_button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    onesie_button.click()

    cart_link = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_link.click()

    checkout_button = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name")))

    first_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#first-name")))
    first_name.send_keys("Ivan")

    last_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#last-name")))
    last_name.send_keys("Ivanov")

    postal_code = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#postal-code")))
    postal_code.send_keys("111111")

    continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue")))
    driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
    time.sleep(0.3)
    driver.execute_script("arguments[0].click();", continue_button)

    wait.until(EC.url_contains("checkout-step-two"))

    assert "checkout-step-two" in driver.current_url

    total_element = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    assert total_element.text is not None