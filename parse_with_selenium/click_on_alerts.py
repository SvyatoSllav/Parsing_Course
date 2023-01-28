import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/blank/modal/2/index.html")
    unique_numbers = set()

    for element in browser.find_elements(By.CLASS_NAME, "buttons"):
        element.click()
        time.sleep(1)
        alert = browser.switch_to.alert
        time.sleep(1)
        alert.accept()
        try:
            result = browser.find_element(By.ID, "result").text
            print(result)
            if result:
                break
        except Exception:
            continue
