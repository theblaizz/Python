from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

element = driver.find_element(By.CSS_SELECTOR, "first-name")

search_input.send_keys("Иван")

element = driver.find_element(By.CSS_SELECTOR, "last-name")

search_input.send_keys("Петров")

element = driver.find_element(By.CSS_SELECTOR, "address")

search_input.send_keys("Ленина, 55-3")

element = driver.find_element(By.CSS_SELECTOR, "e-mail")

search_input.send_keys("test@skypro.com")

element = driver.find_element(By.CSS_SELECTOR, "phone")

search_input.send_keys("+7985899998787")

element = driver.find_element(By.CSS_SELECTOR, "city")

search_input.send_keys("Москва")

element = driver.find_element(By.CSS_SELECTOR, "country")

search_input.send_keys("Россия")

element = driver.find_element(By.CSS_SELECTOR, "job-position")

search_input.send_keys("QA")

element = driver.find_element(By.CSS_SELECTOR, "company")

search_input.send_keys("SkyPro")