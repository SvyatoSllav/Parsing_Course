import requests

from fake_headers import Headers

from fake_useragent import UserAgent

header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="lin",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )

ua = UserAgent()

# Один вариант
response = requests.get(
    url="http://httpbin.org/user-agent",
    headers=header.generate()
)
print(response.text)

# Второй вариант
response = requests.get(
    url="http://httpbin.org/user-agent",
    headers={"user-agent": ua.random}
)

print(response.text)
