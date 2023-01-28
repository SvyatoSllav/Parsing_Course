import requests
import json
from bs4 import BeautifulSoup


def to_bs4_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "lxml")


category_page_url = "https://parsinger.ru/html/index1_page_1.html"
schema = "https://parsinger.ru/html/"

category_page_soup = to_bs4_soup(category_page_url)
pagination_div = category_page_soup.find("div", class_="pagen")
pagination_pages = [tag_a["href"] for tag_a in pagination_div.find_all("a")]

with open("category_products.json", "w", encoding="utf-8") as file:
    result_json = []
    for category_page in pagination_pages:
        category_page_soup = to_bs4_soup(f"{schema}{category_page}")

        all_items = category_page_soup.find("div", class_="item_card").find_all("div", class_="item")
        for item in all_items:
            name = item.find("a", class_="name_item").text.strip()
            description = item.find("div", class_="description").text.split("\n")
            description_ul = [el.split(":")[1].strip() for el in description if el]
            brand = description_ul[0]
            type = description_ul[1]
            material = description_ul[2]
            display_type = description_ul[3]
            price = item.find("p", class_="price").text.strip()
            result_json.append({
                "name": name,
                "brand": brand,
                "type": type,
                "material": material,
                "display_type": display_type,
                "price": price
            })
    json.dump(result_json, file, indent=4, ensure_ascii=False)
