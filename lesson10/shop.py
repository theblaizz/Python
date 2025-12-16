from selenium.webdriver.common.by import By
import allure


@allure.epic("сайт")
@allure.feature("Read")
class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    """
          Конструктор класса Shope.
         :param driver: WebDriver — объект драйвера Selenium.
                """
with allure.step(f"Заполнение данных: имя пользователя,пароль"):

    def login(self, username, password):
        """
                 Вводим данные для входа."""

        username_field = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    with allure.step(f"Добавление карты"):
     def add_product_to_cart(self, product_id):
        add_button = self.driver.find_element(By.CSS_SELECTOR, f"#add-to-cart-{product_id}")
        add_button.click()

    def go_to_cart(self):
        cart_link = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        cart_link.click()

class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, "#checkout")
        checkout_button.click()
    """
         Проверка данных.

         """

class ClientInfoPage:
    def __init__(self, driver):
        self.driver = driver

    with allure.step(f"Заполнение данных: имя,фамилия,индекс"):
     def fill_info(self, first_name, last_name, postal_code):
        first_name_field = self.driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code_field.send_keys(postal_code)

    with allure.step(f"Подтверждение данных"):
     def click_continue(self):
        continue_button = self.driver.find_element(By.CSS_SELECTOR, "#continue")
        continue_button.click()

class ReviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total(self):
        total_element = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        return total_element.text

