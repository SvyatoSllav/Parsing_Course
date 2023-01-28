import requests

url = "https://parsinger.ru/video_downloads/videoplayback.mp4"

with requests.get(url=url, stream=True) as r:
    r.raise_for_status()
    with open('file', 'wb') as video:
        for piece in r.iter_content(chunk_size=8192):
            video.write(piece)

