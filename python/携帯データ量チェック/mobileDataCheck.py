import sys
import tkinter as tk
import pdb
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from datetime import datetime

#ChromeをHeadlessモードで起動
#options = Options()
#options.add_argument('--headless')

#Chromeのパスを指定
#　※Chromedriverが無いとseleniumuは動かない
#　下記パスにあるchromedriver.exeをディレクトリごとコピー
path = r"C:\python\chromedriver\chromedriver.exe"

#Chromeを起動
browser = webdriver.Chrome(path)
#browser = webdriver.Chrome(path,chrome_options=options)
browser.get('https://portal.business.mb.softbank.jp/portal/BPS0001/logout')

#ページが開くまで待つ
time.sleep(1)
#管理者idの入力
admin_name_el = browser.find_element_by_name('authId')
admin_name_el.send_keys('Des19981101')
#パスワードを入力
pwd_el = browser.find_element_by_name('pwd')
pwd_el.send_keys('6350DaisekiEco1101')
#usr_pass_el.submit()

#ログイン処理
time.sleep(0.5)
link_el = browser.find_element_by_class_name('login_btn')
type(link_el)
link_el.click()

#データ容量ページへ移行
time.sleep(0.5)
link_el = browser.find_element_by_class_name('link_a_4')
type(link_el)
link_el.click()

#データ容量ページへ移行
time.sleep(0.5)
link_el = browser.find_elements_by_css_selector('span.btn_next')
#type(link_el)
link_el[2].click()

#回線番号ページへ移行
time.sleep(0.5)
browser.find_elements_by_css_selector('span.btn_next')[1].click()
#type(link_el)

#チェックボックス選択、回線情報移動
browser.find_element_by_name('list[0].checkStatus').click()
browser.find_element_by_id('decision').click()

#データ容量数値取得
#pdb.set_trace() --デバッグ用コード
dataRemain = browser.find_elements_by_class_name('used_td')[1].text
print(dataRemain)

#現在時刻の取得
nowTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(nowTime)

#CSV書き出し
#pdb.set_trace()
f = open("携帯データ量.csv",'a')
writer = csv.writer(f,lineterminator='\n')
writer.writerow([nowTime,dataRemain])
time.sleep(0.5)
f.close()

time.sleep(0.5)
browser.quit()

#time.sleep(0.5)
#exit()