import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/table/3/index.html"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

all_bolds_tags = [float(tag.text) for tag in soup.find_all("b")]
print(sum(all_bolds_tags))
