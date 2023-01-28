import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/table/1/index.html"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

table = soup.find("table").find_all("td")
unique_numbers = set()
for number in table:
    unique_numbers.add(float(number.text))

print(sum(unique_numbers))
