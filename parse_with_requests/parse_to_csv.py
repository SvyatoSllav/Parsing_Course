import requests
import csv
from bs4 import BeautifulSoup


with open("hdd.csv", "w", encoding="utf-8-sig", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        ["Наименование", "Бренд", "Форм-фактор", "Ёмкость", "Объём буф. памяти", "Цена"]
    )

url = "https://parsinger.ru/html/index4_page_1.html"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

# Получаем все страницы в пагинации
schema = "https://parsinger.ru/html/"
pagination_pages = [schema + tag.get("href") for tag in soup.find("div", class_="pagen").find_all("a")]
# Итерируемся по каждой странице
for page in pagination_pages:
    page_response = requests.get(page)
    page_response.encoding = "utf-8"
    page_soup = BeautifulSoup(page_response.text, "lxml")
    # Получаем все hdd
    hdd_items = [item for item in page_soup.find_all("div", class_="item")]

    # Собираем все поля от каждого объекта hdd
    name = [item.find("a", class_="name_item").text.strip() for item in hdd_items]
    description = [[description_el.text for description_el in item.find("div", class_="description").find_all("li")] for item in hdd_items]
    price = [item.find("p", class_="price").text.strip() for item in hdd_items]

    # Записываем данные в файл csv таблицы
    for name, description, price in zip(name, description, price):
        flatten = name, *[el.split(":")[1].strip() for el in description if el], price
        file = open("hdd.csv", "a", encoding="utf-8-sig", newline="")
        writer = csv.writer(file, delimiter=';')
        writer.writerow(flatten)
    file.close()
