from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/expectations/5/index.html")
    browser_waiter = WebDriverWait(browser, 60)
    browser_waiter.until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    elem = browser_waiter.until(EC.presence_of_element_located((By.CLASS_NAME, "Y1DM2GR")))
    print(elem.text)
