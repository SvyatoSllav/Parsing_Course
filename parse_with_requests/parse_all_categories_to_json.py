import requests
import json
from bs4 import BeautifulSoup


def to_bs4_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "lxml")


index_page = "https://parsinger.ru/html/index1_page_1.html"
schema = "https://parsinger.ru/html/"

category_page_soup = to_bs4_soup(index_page)

all_categories_pages_urls = [f"{schema}{tag_a.get('href')}" for tag_a in category_page_soup.find("div", class_="nav_menu").find_all("a")]
categories_pagination_pages = []
for category_page_url in all_categories_pages_urls:
    category_page_soup = to_bs4_soup(category_page_url)
    pagination_div = category_page_soup.find("div", class_="pagen")
    categories_pagination_pages.extend([f"{schema}{tag_a['href']}" for tag_a in pagination_div.find_all("a")])

with open("categories_products.json", "w", encoding="utf-8") as file:
    result_json = []
    for category_page in categories_pagination_pages:
        category_page_soup = to_bs4_soup(category_page)

        all_items = category_page_soup.find("div", class_="item_card").find_all("div", class_="item")
        for item in all_items:
            name = item.find("a", class_="name_item").text.strip()
            description = item.find("div", class_="description").text.split("\n")
            description_ul = [[el.split(":")[0].strip(), el.split(":")[1].strip()] for el in description if el]
            price = item.find("p", class_="price").text.strip()

            item_json = {
                "name": name,
                "price": price
            }
            for description_element in description_ul:
                item_json[description_element[0]] = description_element[1]
            result_json.append(item_json)
    json.dump(result_json, file, indent=4, ensure_ascii=False)
