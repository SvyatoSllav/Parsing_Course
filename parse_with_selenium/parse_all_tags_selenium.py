from selenium import webdriver
from selenium.webdriver.common.by import By


options_crome = webdriver.ChromeOptions()
options_crome.add_argument("--headless")

with webdriver.Chrome(options=options_crome) as browser:
    browser.get("https://parsinger.ru/selenium/3/3.html")
    p_tags = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
    count = 0
    for p_tag in p_tags:
        count += int(p_tag.text)

print(count)
