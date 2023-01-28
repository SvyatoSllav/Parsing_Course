import time
from math import sqrt
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

with webdriver.Chrome() as browser:
    result = 0
    for index in range(len(sites)):
        browser.execute_script(f'window.open("{sites[index]}", "_blank{index}");')
    time.sleep(3)
    for x in range(len(browser.window_handles))[1:]:
        browser.switch_to.window(browser.window_handles[x])
        browser.find_element(By.CLASS_NAME, "checkbox_class").click()
        result += sqrt(int(browser.find_element(By.ID, "result").text))

print(round(result, 9))