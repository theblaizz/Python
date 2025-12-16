from СаclMainPageAllure import CalcMainPage
import allure


@allure.feature("CalcPageAllure")
@allure.title("Нажатие кнопок")
def test_calculator(driver):
 with allure.step(f"Берем функцию из main_page"):
     main_page = CalcMainPage(driver)
 with allure.step(f"Установка задержки 45 секунд"):
        main_page.delay(45)
 with allure.step("Нажатие кнопок"):
        main_page.click_button("7")
        main_page.click_button("+")
        main_page.click_button("8")
        main_page.click_button("=")
 with allure.step(f"проверка результата равенства"):
    assert main_page.get_screen_text() == "15"
