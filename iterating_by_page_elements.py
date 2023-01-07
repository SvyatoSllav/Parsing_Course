import requests

url = "https://parsinger.ru/task/1/"

for i in range(1, 501):
    if requests.get(url=url + f"{i}.html").status_code == 200:
        print(url + f"{i}.html")