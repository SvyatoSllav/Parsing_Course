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

with open("all_products.json", "w", encoding="utf-8") as file:
    result_json = []
    for category_page in categories_pagination_pages:
        category_page_soup = to_bs4_soup(category_page)

        all_items_on_page = category_page_soup.find("div", class_="item_card").find_all("div", class_="item")
        page_item_links = [f"{schema}{item.find('a', class_='name_item').get('href')}" for item in all_items_on_page]
        for item_link in page_item_links:
            item_page_soup = to_bs4_soup(item_link)

            name = item_page_soup.find("p", id="p_header").text.strip()
            article = item_page_soup.find("p", class_="article").text.strip()
            description = item_page_soup.find("ul", id="description").text.split("\n")
            description_ul = [[el.split(":")[0].strip(), el.split(":")[1].strip()] for el in description if el]
            in_stock = item_page_soup.find("span", id="in_stock").text.strip()
            price = item_page_soup.find("span", id="price").text.strip()
            old_price = item_page_soup.find("span", id="old_price").text.strip()
            description_to_json = {}
            for description_element in description_ul:
                description_to_json[description_element[0]] = description_element[1]

            item_json = {
                "categories": "hdd",
                "name": name,
                "article": article,
                "description": description_to_json,
                "count": in_stock,
                "price": price,
                "old_price": old_price,
                "link": item_link
            }

            result_json.append(item_json)
    json.dump(result_json, file, indent=4, ensure_ascii=False)
