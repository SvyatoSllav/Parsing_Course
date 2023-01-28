import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/html/index3_page_1.html"

index_page_res = requests.get(url)
index_page_res.encoding = 'utf-8'

soup = BeautifulSoup(index_page_res.text, 'lxml')

all_pages_links = [tag['href'] for tag in soup.find("div", class_="pagen").find_all('a')]
schema = "https://parsinger.ru/html/"

all_names = []
for link in all_pages_links:
    response = requests.get(f"{schema}{link}")
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    all_names.append([tag.text for tag in soup.find_all('a', class_='name_item')])

print(all_names)
