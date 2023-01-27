from bs4 import BeautifulSoup
import requests


with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")
    print(soup)
