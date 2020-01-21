##  2019/12/14-15  yahoo-HackDay2019 ##

# モジュール(ライブラリ)インポート文
import sys  #環境変数、ほぼ必須
import os   #unixコマンドでOS制御、ほぼ必須
import tkinter.filedialog  #UI作成、フィールドログ
import tkinter.messagebox  #UI作成　メッセージボックス
from PIL import Image,ImageTk  #画像表示、Tkinterで使用する場合
import pdb  #デバッグ用
import time #処理一時停止
from selenium import webdriver #webページ自動操作
from selenium.webdriver.chrome.options import Options  #selenium headlessMode（画面表示しない)
import csv  #csv制御
from datetime import datetime  #時刻表示
import base64 #Base64 データ符号化　[a-z],[A-z]を区別、大文字、小文字判定
import json  #json出力、入力
from requests import Request, Session  #webAPIリクエスト、
from bs4 import BeautifulSoup #ウェブスクレイピング
import re #正規表現操作、文字列マッチングに使用
import smtplib #SMTPプロトコルクライアント、メールアカウントへのアクセスに使用
from email.mime.text import MIMEText #メール自動入力
from email.utils import formatdate #メール設定

#UI作成
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
#tkinter.messagebox.showinfo('molcali','写真の選択をしてください')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

#tkinter.messagebox.showinfo('molcali',file)

path = file

#関数指定　ORC(GoogleAPI)
def recognize_captcha(str_image_path):
        bin_captcha = open(str_image_path, 'rb').read()

        #str_encode_file = base64.b64encode(bin_captcha)
        str_encode_file = base64.b64encode(bin_captcha).decode("utf-8")


        str_url = "https://vision.googleapis.com/v1/images:annotate?key="

        str_api_key = "AIzaSyBRtLnSzC75S-cax1aLv65MaEedrmUjgpc"

        str_headers = {'Content-Type': 'application/json'}

        str_json_data = {
            'requests': [
                {
                    'image': {
                        'content': str_encode_file
                    },
                    'features': [
                        {
                            'type': "TEXT_DETECTION",
                            'maxResults': 10
                        }
                    ]
                }
            ]
        }

        print("begin request")
        obj_session = Session()
        obj_request = Request("POST",
                              str_url + str_api_key,
                              data = json.dumps(str_json_data),
                              headers = str_headers
                              )
        obj_prepped = obj_session.prepare_request(obj_request)
        obj_response = obj_session.send(obj_prepped,
                                        verify=True,
                                        timeout=60
                                        )
        print("end request")

        if obj_response.status_code == 200:
            #print (obj_response.text)
            with open('data.json', 'w') as outfile:
                json.dump(obj_response.text, outfile)
            return obj_response.text
        else:
            return "error"



#--main処理

dataset = []

if __name__ == '__main__':
    data = json.loads(recognize_captcha(path)) 
    data = data["responses"]
    for i in data:
        #print(i["fullTextAnnotation"]["text"])
        #print(i["fullTextAnnotation"])
        dataset.append(i["fullTextAnnotation"]["text"])
        print(dataset)

#例外処理があればここで記載(__name__ =__exeption__ )

Metadataset = "".join(dataset)
print(Metadataset)

#--　ここまでがOCR変換

#Web自動検索

#ChromeをHeadlessモードで起動
options = Options()
options.add_argument('--headless')

#Chromeのパスを指定
#　※Chromedriverが無いとseleniumuは動かない
#　下記パスにあるchromedriver.exeをディレクトリごとコピー
Cpath = r"C:\python\chromedriver\chromedriver.exe"

#Chromeを起動
#browser = webdriver.Chrome(path)
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

#化学式
formulaNmb = targetText.index('化学式')
formula = targetText[formulaNmb + 1]
print('化学式：' + formula)

#モル質量
moler = targetText[formulaNmb + 3]
print('モル質量' + moler)

#沸点
boilingPointNmb = targetText.index('沸点')
boilingPoint = targetText[boilingPointNmb + 1]
print('沸点：' + boilingPoint)

#融点
meltingPointNmb = targetText.index('融点')
meltingPoint = targetText[meltingPointNmb + 1]
print("融点：" + meltingPoint)

#-- ここまでがweb検索

#メール使用　変数代入
account = "itoken0825@gmail.com"
password = "potenz@0825"

to_email = "itoken0825@gmail.com"
from_email = "itoken0825@gmail.com"

#メール本文作成
body = "物質名：" + title[0].text + '\n化学式：' + formula + '\nモル質量：' + moler + '\n沸点：' + boilingPoint + '\n融点：' + meltingPoint

subject = "解析結果"
message = body
msg = MIMEText(message,"html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email

#メール自動送信
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(account,password)
server.send_message(msg)
server.quit() #メールサーバーの操作停止コマンド ※serverは今回の任意変数のため注意

browser.quit() #ブラウザ操作の操作停止コマンド ※server同様、browserは任意変数

exit()

