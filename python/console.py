import sys
import tkinter as tk
import pdb
import time
from selenium import webdriver

def pushedLogin():
    print("login")

def pushedRetire():
    print("Retire")

def newOpen():    
    root = tk.Tk()
    root.title("打刻ツール")
    root.geometry("250x300")

    #ラベルを追加
    #pdb.set_trace()
    label = tk.Label(root,text="勤怠打刻用ツール ver1.0")
    label.grid()

    #ボタン準備
    Adtime = tk.Button(root,text="出勤",font=('',20),command=pushedLogin,fg='#ffffff',bg='#0080ff',width=15,height=3)
    Adtime.grid()
    Retire = tk.Button(root,text="退勤",font=('',20),command=pushedRetire,fg='#ffffff',bg='#ff9f9f',width=15,height=3)
    Retire.grid()

#-----------------------------------------------------------------------------
#出退勤用コンソール
#pdb.set_trace()
root = tk.Tk()
root.title("社員選択")
root.geometry("800x600")


#ラベルを追加
#pdb.set_trace()
label = tk.Label(root,text="勤怠打刻用ツール ver1.0")
label.grid(column=1,row=0)

#ボタン準備
Emp1 = tk.Button(root,text="永淵芳子",font=('',20),command=newOpen,fg='#ffffff',bg='#0080ff',width=10,height=3)
Emp1.grid(column=0,row=1)
Emp2 = tk.Button(root,text="金蔵美津子",font=('',20),command=newOpen,fg='#ffffff',bg='#0080ff',width=10,height=3)
Emp2.grid(column=1,row=1)
Emp3 = tk.Button(root,text="好川伸子",font=('',20),command=newOpen,fg='#ffffff',bg='#0080ff',width=10,height=3)
Emp3.grid(column=2,row=1)


root.mainloop()