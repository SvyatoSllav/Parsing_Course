from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/selenium/6/6.html")
    math_expr_answer = eval(browser.find_element(By.ID, "text_box").text)
    browser.find_element(By.XPATH, f"//option[.='" + str(math_expr_answer) + "']").click()
    browser.find_element(By.CLASS_NAME, "btn").click()
    print(browser.find_element(By.ID, "result").text)
