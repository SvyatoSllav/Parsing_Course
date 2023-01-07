import requests
from bs4 import BeautifulSoup


url = "https://parsinger.ru/table/5/index.html"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

# Создаем словарь с названиями колонок
columns = dict()
for column in soup.find_all("th"):
    columns[column.text] = 0

# Получаем все ряды
all_rows = soup.find_all("tr")[1:]
# Индекс ячейки, для того, чтобы итерироваться по числам в ряду
cell_index = 0
# Итерируемся по каждому полученному ряду
for row in all_rows:
    # Заносим каждое значение ячейки в ряду в словарь со столбцами
    for col in columns.keys():
        columns[col] += float(row.find_all("td")[cell_index].text)
        cell_index += 1
    cell_index = 0

# округляем значения каждого столбца
for col in columns.keys():
    columns[col] = round(columns[col], 3)

print(columns)
