from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

element = driver.find_element(By.CSS_SELECTOR, "delay")

search_input.send_keys("45")

button = driver.find_element_by_class_name('btn-outline-primary >7<')
button.click()

button = driver.find_element_by_class_name('operator btn btn-outline-success')
button.click()

button = driver.find_element_by_class_name('btn-outline-primary >8<')
button.click()

button = driver.find_element_by_class_name('btn btn-outline-warning')
button.click()