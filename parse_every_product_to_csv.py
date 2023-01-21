import requests
import csv
from bs4 import BeautifulSoup


index_page_url = "https://parsinger.ru/html/index1_page_1.html"
schema = "https://parsinger.ru/html/"

index_page_response = requests.get(index_page_url)
index_page_response.encoding = "utf-8"
index_page_soup = BeautifulSoup(index_page_response.text, "lxml")

# Получаем все страницы в пагинации категории часов
watch_pagination_pages = [f"{schema}{tag['href']}" for tag in index_page_soup.find("div", class_="pagen").find_all("a")]

with open("watch.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        [
            "Наименование",
            "Артикул",
            "Бренд",
            "Модель",
            "Тип",
            "Технология экрана",
            "Материал корпуса",
            "Материал браслета",
            "Размер",
            "Сайт производителя",
            "Наличие",
            "Цена",
            "Старая цена",
            "Ссылка на карточку с товаром",
        ]
    )
    for category_page in watch_pagination_pages:
        category_page_res = requests.get(category_page)
        category_page_res.encoding = "utf-8"
        category_page_soup = BeautifulSoup(category_page_res.text, "lxml")
        all_items = category_page_soup.find_all("div", class_="item")
        all_item_links = [f"{schema}{item.find('a', class_='name_item')['href']}" for item in all_items]

        # Итерируемся по каждому товару на странице
        for item_link in all_item_links:
            item_page_response = requests.get(item_link)
            item_page_response.encoding = "utf-8"
            item_page_soup = BeautifulSoup(item_page_response.text, "lxml")

            # Получаем все необходимые поля
            name = item_page_soup.find("p", id="p_header").text.strip()
            article = item_page_soup.find("p", class_="article").text.split(":")[1].strip()
            description_ul = item_page_soup.find("ul", id="description").text.split("\n")
            description = [desc_el.split(":")[1].strip() for desc_el in description_ul if desc_el]
            in_stock = item_page_soup.find("span", id="in_stock").text.split(":")[1].strip()
            price = item_page_soup.find("span", id="price").text.strip()
            old_price = item_page_soup.find("span", id="old_price").text.strip()

            # Заносим в csv таблицу
            flatten = name, article, *description, in_stock, price, old_price, item_link
            writer.writerow(flatten)
