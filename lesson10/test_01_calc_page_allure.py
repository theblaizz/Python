from СаclMainPageAllure import CalcMainPage
import allure

def test_calculator(driver):
    main_page = MainPage(driver)(f"Берем функцию из main_page")

    main_page.delay(45)(f"Установка задержки {delay} секунд")

    main_page.click_button('7')
    main_page.click_button('+')
    main_page.click_button('8')
    main_page.click_button('=')
    (f"Нажатие кнопок: {num1}, {operation}, {num2}, '='")
    assert main_page.get_screen_text() == "15"("Проверка результата")
    (f"Ожидаемый результат: {15})