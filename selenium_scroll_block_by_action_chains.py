import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/infiniti_scroll_1/")
    scroll_container = browser.find_element(By.ID, "scroll-container")
    all_nums = set()
    while True:
        time.sleep(1)
        span_elements = scroll_container.find_elements(By.TAG_NAME, "span")
        time.sleep(1)
        last_tag_span = span_elements[-1]
        for span_tag in span_elements:
            all_nums.add(int(span_tag.text))
        if last_tag_span.get_attribute("class") == "last-of-list":
            break
        ActionChains(browser).move_to_element(last_tag_span).perform()

print(sum(all_nums))
