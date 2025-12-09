from shop import *

def test_saucedemo_shopping(driver):
    auth_page = AuthPage(driver)
    auth_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_product_to_cart("sauce-labs-backpack")
    products_page.add_product_to_cart("sauce-labs-bolt-t-shirt")
    products_page.add_product_to_cart("sauce-labs-onesie")

    products_page.go_to_cart()

    cart_page = ShoppingCartPage(driver)
    cart_page.checkout()

    client_info_page = ClientInfoPage(driver)
    client_info_page.fill_info("Ivan", "Ivanov", "111111")

    client_info_page.click_continue()
    review_page = ReviewPage(driver)

    assert review_page.get_total() == "Total: $58.29"