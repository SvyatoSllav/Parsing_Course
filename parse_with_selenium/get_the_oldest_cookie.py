import time

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

schema = "https://parsinger.ru/methods/5/"

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/methods/5/index.html")
    links = [div.find_element(By.TAG_NAME, "a").get_attribute("href") for div in browser.find_elements(By.CLASS_NAME, "urls")]

    browser.get(links[0])
    most_outdated_cookie = time.strftime('%Y-%m-%d', time.localtime(browser.get_cookies()[0].get("expiry")))
    most_outdated_num = browser.find_element(By.ID, "result").text
    for link in links[1:]:
        browser.get(link)
        cookie_date = time.strftime('%Y-%m-%d', time.localtime(browser.get_cookies()[0].get("expiry")))
        if cookie_date > most_outdated_cookie:
            most_outdated_cookie = cookie_date
            most_outdated_num = browser.find_element(By.ID, "result").text

print(most_outdated_num)
