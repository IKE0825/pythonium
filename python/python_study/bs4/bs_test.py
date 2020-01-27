import requests
from bs4 import BeautifulSoup as bs4
import pdb

url = "https://docs.python.org/ja/3/library/index.html"

res = requests.get(url)
soup = bs4(res.content,"html.parser")

uls = soup.find_all("ul")

lst_uls = []

for ul in uls:
    #print(ul.text)
    lst_uls.append(ul.text)

print(lst_uls)