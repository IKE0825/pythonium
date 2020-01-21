from PIL import Image

# 画像ファイルを開く
im = Image.open('KIMG0130.jpg')
# EXIF情報を得る
exif = im._getexif()
# 一覧で表示
for id, value in exif.items():
    print(id, value)