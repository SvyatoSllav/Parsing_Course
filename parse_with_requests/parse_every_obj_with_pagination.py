import requests
from bs4 import BeautifulSoup


index_page_url = "https://parsinger.ru/html/index3_page_4.html"

index_page_res = requests.get(index_page_url)
index_page_res.encoding = "utf-8"
soup = BeautifulSoup(index_page_res.text, "lxml")

all_pagination_links = [tag["href"] for tag in soup.find("div", class_="pagen").find_all('a')]
schema = "https://parsinger.ru/html/"

all_products_links = []
for link in all_pagination_links:
    response = requests.get(f"{schema}{link}")
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'lxml')
    all_items_a_tags = soup.find('div', class_='item_card').find_all('a', class_="name_item")
    all_products_links.append([tag["href"] for tag in all_items_a_tags])

all_articles = []
sum_of_articles = 0
for page_product_links in all_products_links:
    for product_link in page_product_links:
        product_response = requests.get(f"{schema}{product_link}")
        product_response.encoding = "utf-8"
        soup = BeautifulSoup(product_response.text, 'lxml')
        sum_of_articles += int(soup.find('p', class_="article").text.split(':')[1])

print(sum_of_articles)
