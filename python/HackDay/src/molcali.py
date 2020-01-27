import sys
import os
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image,ImageTk
import pdb
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from datetime import datetime
import base64
import json
from requests import Request, Session
from bs4 import BeautifulSoup
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
#tkinter.messagebox.showinfo('molcali','写真の選択をしてください')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

#tkinter.messagebox.showinfo('molcali',file)

path = file

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

#pdb.set_trace()
dataset = []
if __name__ == '__main__':
    data = json.loads(recognize_captcha(path))
    #print(data)
    data = data["responses"]
    #print(data)
    for i in data:
        #print(i["fullTextAnnotation"]["text"])
        #print(i["fullTextAnnotation"])
        dataset.append(i["fullTextAnnotation"]["text"])
        print(dataset)


#Mdataset = "".join(dataset)
#Mdataset = re.compile(Mdataset)

#matchresult = Mdataset.findall("Na2SO4adb")

#print(matchresult)


Mdataset = "".join(dataset)
#Sdataset1 = re.sub(r'\^a-zA-Z0-9_',"",Mdataset)

#Mdataset = "".join(dataset)
#Sdataset1 = re.sub('\^a-zA-Z0-9_',"",Mdataset)

print(Mdataset)

#ChromeをHeadlessモードで起動
#pdb.set_trace()
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
#pdb.set_trace()
time.sleep(0.1)
inputBox = browser.find_element_by_id('ooui-php-1')
inputBox.send_keys(Mdataset)
link_el = browser.find_element_by_class_name('oo-ui-actionFieldLayout-button')
link_el.click()

#検索ページでの選択
time.sleep(0.1)
#pdb.set_trace()
#link_el = browser.find_elements_by_class_name('mw-redirect')
link_el = browser.find_elements_by_xpath("//div/div/div/div/ul/li/div/a")
print(link_el[0])
link_el[0].click()

#化学式ページ閲覧
time.sleep(0.5)
#pdb.set_trace()

#物質名取得
title = browser.find_elements_by_css_selector("h1")
#print(title[0].text)

value = browser.find_elements_by_tag_name('td')
targetText = []

for i in value:
    addtext = i.text
    #print(addtext)
    targetText.append(addtext)
    #print(targetText)

print('物質名：' + title[0].text)

#print(targetText.index('化学式'))
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

account = "itoken0825@gmail.com"
password = "potenz@0825"

to_email = "itoken0825@gmail.com"
from_email = "itoken0825@gmail.com"

body = "物質名：" + title[0].text + '\n化学式：' + formula + '\nモル質量：' + moler + '\n沸点：' + boilingPoint + '\n融点：' + meltingPoint
#print(body)

subject = "解析結果"
message = body
msg = MIMEText(message,"html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email

server = smtplib.SMTP('smtp.gmail.com', 587)
#smtpobj.set_debuglevel(True)
server.starttls()
server.login(account,password)
server.send_message(msg)
server.quit()

browser.quit()

exit()

"""
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

"""