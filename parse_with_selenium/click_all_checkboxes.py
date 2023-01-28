from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/selenium/4/4.html")
    [checkbox.click() for checkbox in browser.find_elements(By.CLASS_NAME, "check")]
    browser.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(3)
    print(browser.find_element(By.ID, "result").text)