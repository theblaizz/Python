from calculator import MainPage


def test_calculator(driver):
    main_page = MainPage(driver)

    main_page.delay(45)

    main_page.click_button('7')
    main_page.click_button('+')
    main_page.click_button('8')
    main_page.click_button('=')

    assert main_page.get_screen_text() == "15"