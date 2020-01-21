#事前準備　ターミナルで下記コマンド
#pip install selenium  ライブラリ"selenium"インストール
#pip install chromedriver-binary
#chromedriverはchromeのバージョンと同じものを使用すること

#デバッグ用ライブラリ
import pdb
#処理ステップ管理用ライブラリ
import time

from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expcepted_conditions as EC
#from selenium.common.exceptions import TimeoutException

#Chromeのパスを指定
path = r"C:\Users\ec000248\AppData\Local\Programs\Python\Python37\Lib\site-packages\chromedriver_binary\chromedriver.exe"

#Chromeを起動
browser = webdriver.Chrome(path)
#pdb.set_trace()

#ブラウザを開く
browser.get('https://cl.i-abs.co.jp/s-clocking/login.asp')
#ページが開くまで待つ
time.sleep(1)
#企業idの入力
company_name_el = browser.find_element_by_name('inDataSource')
company_name_el.send_keys('daisekieco')
#ユーザー名の入力
usr_name_el = browser.find_element_by_name('inEmpCode')
usr_name_el.send_keys('248')
#パスワードの入力
usr_pass_el = browser.find_element_by_name('inPassWord')
usr_pass_el.send_keys('potenza0825')
#usr_pass_el.submit()
#pdb.set_trace()
#WebDriverWait(browser,30).until(EC.presence_of_element_located(By.ID,'login')
time.sleep(0.5)
link_el = browser.find_element_by_id('login')
type(link_el)
link_el.click()

#打刻ページへの移動
#WebDriverWait(browser,30).until(EC.presence_of_element_located(By.ID,'Item2')
time.sleep(0.5)
link_el = browser.find_element_by_id('Item2')
link_el.click()

#デバッグコード
#pdb.set_trace()

#打刻実行
#WebDriverWait(browser,30).until(EC.presence_of_element_located(By.ID,'tdbtnEnter')
time.sleep(0.5)
link_el = browser.find_element_by_id('imgAtt1')
link_el.click()
link_el = browser.find_element_by_id('tdbtnEnter')
link_el.click()
time.sleep(0.5)
link_el = browser.find_element_by_id('tdbtnOK')
link_el.click()

#ブラウザ終了
time.sleep(1.0)
#pdb.set_trace()
browser.close()