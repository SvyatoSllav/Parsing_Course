from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/selenium/7/7.html")
    drop_down_el_sum = sum([int(num.text) for num in browser.find_elements(By.TAG_NAME, "option")])
    browser.find_element(By.ID, "input_result").send_keys(drop_down_el_sum)
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, "result").text)
