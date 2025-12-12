from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcMainPage:

    def __init__(self, driver):
        """
         Конструктор класса CalcMainPage.
        :param driver: WebDriver — объект драйвера Selenium.
               """
        self._driver = driver

        @allure.step("Открытие страницы калькулятора")
        """
               Открывает страницу калькулятора.
               """
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(2)
        self._driver.maximize_window()

    @allure.step("Установка задержки {delay} секунд")
    """
         Устанавливает задержку для выполнения операций на калькуляторе.

         :param delay: int — время задержки в секундах.
         """
    def delay(self, seconds):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    @allure.step("Нажатие кнопки '{button}'")
    """
          Нажимает на кнопку калькулятора.

          :param button: str — текст на кнопке, которую нужно нажать.
          """
    def click_button(self, button_text):
        button = self._driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    @allure.step("Ожидание результата '{expected_result}'")
    """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param expected_result: str — ожидаемый результат.
        :param delay: int — время задержки в секундах.
        """

    def get_screen_text(self):
        wait = WebDriverWait(self._driver, 50)

        @allure.step("Получение результата с экрана калькулятора")

        """
            Возвращает текущий результат с экрана калькулятора.

            :return: str — текст результата на экране калькулятора.
            """
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        screen = self._driver.find_element(By.CSS_SELECTOR, ".screen")
        return screen.text








