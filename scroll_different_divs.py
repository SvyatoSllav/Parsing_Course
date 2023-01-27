import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/infiniti_scroll_3/")
    scroll_elements = []
    for scroll_number in range(1, 6):
        scroll_element = browser.find_element(By.XPATH, f'//*[@id="scroll-container_{scroll_number}"]/div')
        print(scroll_element)
        time.sleep(2)
        for scroll in range(10):
            ActionChains(browser).move_to_element(scroll_element).scroll_by_amount(1, 500).perform()
    result = sum([int(tag_span.text) for tag_span in browser.find_elements(By.TAG_NAME, "span")])

print(result)
