import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/window_size/2/index.html")
    for x_cord in window_size_x:
        for y_cord in window_size_y:
            browser.set_window_size(x_cord, y_cord)
            if browser.find_element(By.ID, "result").text:
                print(browser.get_window_size())
                break
