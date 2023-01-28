import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/table/5/index.html"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

all_rows = [row for row in soup.find_all("tr")][1:]
sum_of_orange_and_blue_composition = 0
for row in all_rows:
    orange_el = float(row.find("td", class_="orange").text)
    blue_el = float(row.find_all("td")[-1].text)
    sum_of_orange_and_blue_composition += orange_el * blue_el

print(sum_of_orange_and_blue_composition)
