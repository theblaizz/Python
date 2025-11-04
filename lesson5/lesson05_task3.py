from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("http://the-internet.herokuapp.com/inputs")

element = browser.find_element(By.CSS_SELECTOR, "#numder")

search_input.send_keys("Sky")

numder_input.clear()

element = browser.find_element(By.CSS_SELECTOR, "#numder")

search_input.send_keys("Pro")

quit()