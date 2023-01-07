import requests


url = 'http://httpbin.org/ip'
proxy = {
    'http': 'http://78.38.28.239',
    'https': 'http://78.38.28.239',

}

response = requests.get(url=url)
print(response.json())