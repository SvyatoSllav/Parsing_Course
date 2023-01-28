import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/blank/modal/3/index.html")
    unique_numbers = set()
    input = browser.find_element(By.ID, "input")
    submit_btn = browser.find_element(By.ID, "check")
    for element in browser.find_elements(By.CLASS_NAME, "buttons"):
        element.click()
        alert = browser.switch_to.alert
        text = alert.text
        alert.accept()
        try:
            input.send_keys(text)
            submit_btn.click()
            result = browser.find_element(By.ID, "result")
            if result.text != "Неверный пин-код":
                print(result.text)
                break
        except Exception:
            continue
