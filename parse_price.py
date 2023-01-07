import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/html/index1_page_1.html"

res = requests.get(url)
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, "lxml")

all_price_tags = soup.find_all('p', class_='price')

all_price_content = [int(p_tag.text.split()[0]) for p_tag in all_price_tags]

print(sum(all_price_content))
