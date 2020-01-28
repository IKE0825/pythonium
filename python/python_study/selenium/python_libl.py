import sys
import pdb
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from bs4 import BeautifulSoup
import requests

#ChromeをHeadlessモードで起動
#options = Options()
#options.add_argument('--headless')

#Chromeのパスを指定
#　※Chromedriverが無いとseleniumuは動かない
#　下記パスにあるchromedriver.exeをディレクトリごとコピー

#リンク取得
res = requests.get("https://docs.python.org/ja/3/library/index.html")
soup = BeautifulSoup(res.content,"html.parser")

links = soup.find_all(class_ = "reference internal")

nmlinks = len(links)
print(nmlinks)

lstLink =[]

for i in range(nmlinks):
    linkElem = links[i].text
    lstLink.append(linkElem)
    #linkText = links[].text
    #print(linkText)

print(lstLink)

#ブラウザ自動操作
path = r"C:\python\chromedriver\chromedriver.exe"

#linuxの場合はpath指定不要
#binファイル内にchromedriverを格納 "sudo mv chromedriver /usr/local/bin"
#おまじない "sudo chown root:root /usr/local/bin/chromedriver"

#Windowsの場合、pathを指定
browser = webdriver.Chrome(path)
browser.get("https://docs.python.org/ja/3/library/index.html")

urls = []

time.sleep(1)

#pdb.set_trace()

for i in range(nmlinks):
    selLink = lstLink[i]
    element = browser.find_element_by_link_text(selLink)
    element.click()
    cur_url = browser.current_url
    urls.append(cur_url)
    browser.back()

print(urls)
