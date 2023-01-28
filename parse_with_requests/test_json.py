import requests

from pprint import pprint


response = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
pprint(response.json())
