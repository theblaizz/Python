from Mainpage import MainPage
import pytest
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()

    button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()

    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()

    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    wait = WebDriverWait(driver, 50)
    result = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    screen = driver.find_element(By.CSS_SELECTOR, ".screen")
    assert screen.text == "15"