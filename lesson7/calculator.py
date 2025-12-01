from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(2)
        self._driver.maximize_window()

    def delay(self, seconds):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, button_text):
        button = self._driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def get_screen_text(self):
        wait = WebDriverWait(self._driver, 50)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        screen = self._driver.find_element(By.CSS_SELECTOR, ".screen")
        return screen.text