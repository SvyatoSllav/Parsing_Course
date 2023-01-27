import requests


for num in range(1, 160):
    url = "https://parsinger.ru/img_download/img/ready/{number}.png"
    with open(f"img_{i}.png", "wb") as file:
        f = file.write(requests.get(url.format(number=i)).content)
        print(i)
