import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/table/2/index.html"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

first_columns = [tag for tag in soup.find_all("tr")]
sum_of_first_numbers = 0
for col in range(1, 17):
    print(float(first_columns[col].find_all("td")[0].text))
    sum_of_first_numbers += float(first_columns[col].find_all("td")[0].text)
print(sum_of_first_numbers)
