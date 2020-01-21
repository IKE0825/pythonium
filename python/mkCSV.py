import os, csv, time

listFile = 'filelist.csv'
dateFormat = '%Y/%m/%d %H:%M:%S'

csvFile = open(listFile, 'w', newline='')
csvWriter = csv.writer(csvFile)

for filename in os.listdir():
    
    if os.path.isfile(filename) \
       and os.path.basename(__file__) != filename \
       and listFile != filename:
        row = []
        # ファイル名
        row.append(filename)
        # ファイル作成日時
        row.append(time.strftime(dateFormat, \
                   time.localtime(os.path.getctime(filename))))
        # ファイル更新日時
        row.append(time.strftime(dateFormat, \
                   time.localtime(os.path.getmtime(filename))))

        csvWriter.writerow(row)

csvFile.close()