import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/infiniti_scroll_2/")
    scroll_container = browser.find_element(By.ID, "scroll-container")
    all_nums = set()
    while True:
        time.sleep(1)
        p_elements = scroll_container.find_elements(By.TAG_NAME, "p")
        time.sleep(1)
        last_tag_p = p_elements[-1]
        for p_tag in p_elements:
            all_nums.add(int(p_tag.text))
        if last_tag_p.get_attribute("class") == "last-of-list":
            break
        ActionChains(browser).move_to_element(last_tag_p).perform()

print(sum(all_nums))
