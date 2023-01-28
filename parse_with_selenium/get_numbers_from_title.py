import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    result = 0
    browser.get("https://parsinger.ru/blank/3/index.html")
    for btn in browser.find_elements(By.CLASS_NAME, "buttons"):
        btn.click()
        # time.sleep(1)
        # print(browser.title)
    for x in range(len(browser.window_handles))[1:]:
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        result += int(browser.execute_script("return document.title;"))

print(result)
