import requests
import csv
from bs4 import BeautifulSoup


index_page_url = "https://parsinger.ru/html/index1_page_1.html"

index_page_response = requests.get(index_page_url)
index_page_response.encoding = "utf-8"
index_page_soup = BeautifulSoup(index_page_response.text, "lxml")

categories_urls = [tag.get("href") for tag in index_page_soup.find("div", class_="nav_menu").find_all("a")]
schema = "https://parsinger.ru/html/"
category_pagination_urls = list()
# Получаем все ссылки из пагинации по каждой категории
for category_url in categories_urls:
    category_page_res = requests.get(f"{schema}{category_url}")
    category_page_res.encoding = "utf-8"
    category_page_soup = BeautifulSoup(category_page_res.text, "lxml")
    nav_menu_a_tags = category_page_soup.find("div", class_="pagen").find_all("a")
    category_pagination_urls.append([tag.get("href") for tag in nav_menu_a_tags])

# Создаем csv таблицу
with open("all_items.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    # Итерируемся по списку страниц в пагинации категории
    for category_pages in category_pagination_urls:
        # Итерируемся по каждой странице в пагинации категории
        for category_page in category_pages:
            category_page_res = requests.get(f"{schema}{category_page}")
            category_page_res.encoding = "utf-8"
            category_page_soup = BeautifulSoup(category_page_res.text, "lxml")

            # Получаем все товары на странице
            all_items_on_page = category_page_soup.find_all("div", class_="item")
            for item in all_items_on_page:
                # Получаем каждый товар и заносим в таблицу его данные
                name = item.find("a", class_="name_item").text.strip()
                desc = [tag.text.split("\n") for tag in item.find("div", class_="description")]
                price = item.find("p", class_="price").text.strip()
                flatten = name, *[el[0].split(":")[1].strip() for el in desc if el[0]], price
                writer.writerow(flatten)
