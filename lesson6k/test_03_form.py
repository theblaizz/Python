from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("https://www.saucedemo.com")

element = browser.find_element(By.CSS_SELECTOR, "user-name")

search_input.send_keys("standard_user")

element = browser.find_element(By.CSS_SELECTOR, "password")

search_input.send_keys("secret_sauce")

button = driver.find_element_by_class_name('submit-button btn_action')
button.click()


button = driver.find_element_by_class_name('add-to-cart-sauce-labs-backpack')
button.click()

button = driver.find_element_by_class_name('add-to-cart-sauce-labs-bolt-t-shirt')
button.click()

button = driver.find_element_by_class_name('add-to-cart-sauce-labs-onesie')
button.click()

button = driver.find_element_by_class_name('shopping_cart_link')
button.click()

button = driver.find_element_by_class_name('btn btn_action btn_medium checkout_button ')
button.click()

browser.get("http://the-internet.herokuapp.com/inputs")

element = browser.find_element(By.CSS_SELECTOR, "first-name")

search_input.send_keys("Иван")

numder_input.clear()

element = browser.find_element(By.CSS_SELECTOR, "last-name")

search_input.send_keys("Иванов")

element = browser.find_element(By.CSS_SELECTOR, "postal-code")

search_input.send_keys("111111")

button = driver.find_element_by_class_name('submit-button btn btn_primary cart_button btn_action')
button.click()

quit()