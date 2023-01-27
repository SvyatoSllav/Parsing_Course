from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get("https://parsinger.ru/scroll/3/")

    items = browser.find_elements(By.CLASS_NAME, "item")
    result = 0
    for item_index in range(len(items)):
        item = items[item_index]
        checkbox = item.find_element(By.CLASS_NAME, "checkbox_class")
        ActionChains(browser).move_to_element(checkbox).click().perform()
        number = item.find_element(By.ID, f"result{item_index+1}").text
        if number:
            result += int(checkbox.get_attribute("id"))

print(result)
