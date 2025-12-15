from shop import *


@allure.feature("shopPageAllure")
def test_saucedemo_shopping(driver):
    auth_page = AuthPage(driver)
    auth_page.login("standard_user", "secret_sauce")

    with allure.step(f"добавление в корзину"):
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart("sauce-labs-backpack")
    products_page.add_product_to_cart("sauce-labs-bolt-t-shirt")
    products_page.add_product_to_cart("sauce-labs-onesie")

    products_page.go_to_cart()

    cart_page = ShoppingCartPage(driver)
    cart_page.checkout()
    """
           Заполнение данных.
     """
    with allure.step(f"Заполнение данных): {username},{last_name},{postal_code}"):
    client_info_page = ClientInfoPage(driver)
    client_info_page.fill_info("Ivan", "Ivanov", "111111")

    client_info_page.click_continue()
    review_page = ReviewPage(driver)
    """
         Возвращает текущий результат с экрана.

        :return: str — текст с суммой результата на экране.
     """
    assert review_page.get_total() == "Total: $58.29"
