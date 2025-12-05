from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()

browser.get("http://the-internet.herokuapp.com/login")

search_locator = "#text"

element = browser.find_element(By.CSS_SELECTOR, "input#username")

search_input.send_keys("tomsmith")
