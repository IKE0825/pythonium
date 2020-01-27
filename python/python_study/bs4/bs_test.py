import requests
from bs4 import BeautifulSoup as bs4

url = "https://used.dospara.co.jp/sale/search.php?view=1&br=11&cbr=1102&page=1"

res = requests.get(url)
soup = bs4(res.text)

dls = soup.find_all("dl")

for dl in dls:
    print(dl.text)
