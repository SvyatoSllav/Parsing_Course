import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/html/hdd/4/4_1.html"

res = requests.get(url)
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, 'lxml')

new_price = int(soup.find('span', id='price').text.split()[0])
old_price = int(soup.find('span', id='old_price').text.split()[0])
print((old_price-new_price) * 100 / old_price)
