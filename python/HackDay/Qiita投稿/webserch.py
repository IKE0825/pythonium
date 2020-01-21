#Web自動検索

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  #selenium headlessMode（画面表示しない)

Metadataset = "NaOH" #ここにOCRで得たテキスト値を入力

#ChromeをHeadlessモードで起動
options = Options()
options.add_argument('--headless')

#Chromeのパスを指定
#　※Chromedriverが無いとseleniumuは動かない
#　下記パスにあるchromedriver.exeをディレクトリごとコピー
Cpath = r"C:\python\chromedriver\chromedriver.exe"

#Chromeを起動
browser = webdriver.Chrome(Cpath,chrome_options=options)
browser.get('https://ja.wikipedia.org/w/index.php?search=&title=%E7%89%B9%E5%88%A5%3A%E6%A4%9C%E7%B4%A2&go=%E8%A1%A8%E7%A4%BA')

#ページが開くまで待つ
time.sleep(0.5)

#検索入力
time.sleep(0.1)
inputBox = browser.find_element_by_id('ooui-php-1') #htmlで要素idが'ooui-php-1'の要素を取得(検索ボックスの場所取得)
inputBox.send_keys(Metadataset) #取得したInputBoxの場所に変数：Metadatasetの値を入力
link_el = browser.find_element_by_class_name('oo-ui-actionFieldLayout-button')
link_el.click()

#検索ページでの選択
time.sleep(0.1)
link_el = browser.find_elements_by_xpath("//div/div/div/div/ul/li/div/a")
print(link_el[0])
link_el[0].click()

#化学式ページ閲覧
time.sleep(0.5)
title = browser.find_elements_by_css_selector("h1")
value = browser.find_elements_by_tag_name('td')

targetText = []

#リストtargetTextにvalueをリストとして格納
#リストに格納するのは、表示項目を指定するため（'化学式'の次の項目を拾う 等)

for i in value:
    addtext = i.text #i個目の要素をaddtextとする
    targetText.append(addtext)

#物質名
print('物質名：' + title[0].text)

#ほんとは例外処理が必要(インデックスで見つからなかったとき)

#化学式
formulaNmb = targetText.index('化学式')
formula = targetText[formulaNmb + 1]
print('化学式：' + formula)

#モル質量
moler = targetText[formulaNmb + 3] #化学式の下にモル質量が書いてあったので横着した
print('モル質量' + moler)

#沸点
boilingPointNmb = targetText.index('沸点')
boilingPoint = targetText[boilingPointNmb + 1]
print('沸点：' + boilingPoint)

#融点
meltingPointNmb = targetText.index('融点')
meltingPoint = targetText[meltingPointNmb + 1]
print("融点：" + meltingPoint)