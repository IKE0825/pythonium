# -*- coding: utf-8 -*-
###############################################################################
# ライブラリインポート
###############################################################################
import os                       # os の情報を扱うライブラリ
import pytesseract              # tesseract の python 用ライブラリ
from PIL import Image           # 画像処理ライブラリ
import pdb
 
# グレースケール変換関数
def ConversionGrayScale(img):
    gray_img = img.convert('L')
    return gray_img
 
# 二値化（値が 200 未満は 0 にする）関数
def BinarizationImage(img):
    WhiteOnBlack_img = img.point(lambda x:0 if x < 100 else x)
    return WhiteOnBlack_img
 
# カレントディレクトリを変更する
os.chdir(r"C:\Users\ec000248\Downloads\2019-12-14")
 
# ファイル名定義
Image000 = 'KIMG0142.jpg'
Image020 = '020_WhiteOnBlack_Const_Image.jpg'
 
# pytesseract に tesseract のパスを通す
# pytesseract.tesseract_cmd='C:\Program Files\Tesseract-OCR\tesseract.exe'
 
#################### 画像の読み込み ####################
pdb.set_trace()
img = Image.open(Image000)
 
# グレースケール変換
gray_img = ConversionGrayScale(img)
 
# 二値化
Black_img = BinarizationImage(gray_img)
Black_img.save(Image020)

quit()
exit()
