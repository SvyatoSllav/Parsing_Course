import requests
import csv
from bs4 import BeautifulSoup

url = "https://parsinger.ru/html/index4_page_1.html"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
