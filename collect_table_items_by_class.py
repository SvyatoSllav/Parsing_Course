import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/4/index.html"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

green_cells = [float(num.text) for num in soup.find_all("td", class_="green")]
print(sum(green_cells))
