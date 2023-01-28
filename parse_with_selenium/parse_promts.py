import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/blank/modal/4/index.html")
    for element in browser.find_elements(By.CLASS_NAME, "pin"):
        element_text = str(element.text)
        browser.find_element(By.ID, "check").click()
        prompt = browser.switch_to.alert
        prompt.send_keys(element_text)
        prompt.accept()
        try:
            result = browser.find_element(By.ID, "result")
            if result.text != "Неверный пин-код":
                print(result.text)
                break
        except Exception:
            continue
