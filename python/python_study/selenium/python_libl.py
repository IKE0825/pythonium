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

res = requests.get("https://docs.python.org/ja/3/library/index.html")
soup = BeautifulSoup(res.content,"html.parser")

links = soup.find_all(class_ = "reference internal")
linkText = links[2].text
print(linkText)

path = r"C:\python\chromedriver\chromedriver.exe"
#linuxの場合はpath指定不要
#binファイル内にchromedriverを格納 "sudo mv chromedriver /usr/local/bin"
#おまじない "sudo chown root:root /usr/local/bin/chromedriver"

#indowsの場合、pathを指定
browser = webdriver.Chrome()
browser.get("https://docs.python.org/ja/3/library/index.html")

urls = []

time.sleep(1)

pdb.set_trace()

element = browser.find_elements_by_link_text(linkText)
print(element)
