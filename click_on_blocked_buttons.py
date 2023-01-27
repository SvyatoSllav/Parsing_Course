from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/scroll/4/index.html")
    unique_numbers = set()

    for element in browser.find_elements(By.CLASS_NAME, "btn"):
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        unique_numbers.add(int(browser.find_element(By.ID, "result").text))

print(sum(unique_numbers))
