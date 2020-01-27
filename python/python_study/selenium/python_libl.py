import requests
from bs4 import BeautifulSoup as bs4
import pdb

url = "https://docs.python.org/ja/3/library/index.html"

res = requests.get(url)
soup = bs4(res.content,"html.parser")

uls = soup.find_all(class_ = "toctree-l2")
links = soup.find_all(class_ = "reference internal")

lst_uls = []
lst_link = []

for ul in uls:
    #print(ul.text)
    lst_uls.append(ul.text)

for link in links:
    url = link.get("href")
    lst_link.append(url)

#print(lst_uls)

print(lst_link)
