from concurrent.futures import ThreadPoolExecutor
import urllib.request as ur

datas = []

def get_from(url):
    connection = ur.urlopen(url)
    data = connection.read()
    datas.append(url)
    datas.append(data)

urls = [
    "https://python.org",
    "https://docs.python.org/"
    "https://wikipedia.org",
    "https://imdb.com",    
]

with ThreadPoolExecutor() as ex:
    for url in urls:
        ex.submit(get_from, url)

print ([str(_[:200])+"\n\n\n" for _ in datas])