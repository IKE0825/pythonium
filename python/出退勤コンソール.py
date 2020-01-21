import sys
import tkinter as tk
import pdb
import time
from selenium import webdriver

#Chromeのパスを指定
path = r"C:\Users\ec000248\AppData\Local\Programs\Python\Python37\Lib\site-packages\chromedriver_binary\chromedriver.exe"

#出勤ファンクション
def pushedLogin():
    #Chromeを起動
    browser = webdriver.Chrome(path)
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
    link_el = browser.find_element_by_id('imgAtt0')
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

    #システム終了
    sys.exit()

#退勤ファンクション
def pushedRetire():
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

    #システム終了
    sys.exit()

#-----------------------------------------------------------------------------
#出退勤用コンソール
#pdb.set_trace()
root = tk.Tk()
root.title("打刻ツール")
root.geometry("250x250")

#ラベルを追加
#pdb.set_trace()
label = tk.Label(root,text="勤怠打刻用ツール ver1.0")

#表示
label.grid()

#ボタン準備
Adtime = tk.Button(root,text="出勤",font=('',20),command=pushedLogin,fg='#ffffff',bg='#0080ff',width=15,height=3)
Adtime.grid()
Retire = tk.Button(root,text="退勤",font=('',20),command=pushedRetire,fg='#ffffff',bg='#ff9f9f',width=15,height=3)
Retire.grid()

root.mainloop()