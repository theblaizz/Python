from СаclMainPageAllure import CalcMainPage
import allure


@allure.feature("CalcPageAllure")
def test_calculator(driver):
    with allure.step(f"Берем функцию из main_page")
    main_page = MainPage(driver)
    with allure.step(f"Установка задержки {delay} секунд")
        main_page.delay(45)
@allure.title("Нажатие кнопок")
    main_page.click_button('7')
    main_page.click_button('+')
    main_page.click_button('8')
    main_page.click_button('=')
    with allure.step(f"Нажатие кнопок: {num1}, {operation}, {num2}, '='")
    assert main_page.get_screen_text() == "15"("Проверка результата")
    (f"Ожидаемый результат: {15})