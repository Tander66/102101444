import numpy as np
import xlwt
from collections import Counter

f = open('B站弹幕.txt','r',encoding= 'utf-8')
a = f.read()
list = a.split("\n")
counter = Counter(list) #对每种弹幕进行计数
top = counter.most_common() #按出现次数从多到少排序弹幕
#创建sheet
data = np.random.randint(999999, size=(10000, 2))
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)


col = ['编号','弹幕', '出现次数']
for c in range(len(col)):
    sheet.write(0, c, col[c]) #创建第一行的三列为'编号','弹幕', '出现次数'
for i in range(len(top)):
    sheet.write(i + 1, 0, i + 1) #此处为每一行的编号
    sheet.write(i + 1, 1, top[i][0]) #此处为每一行的弹幕内容
    sheet.write(i + 1, 2, top[i][1]) #此处为每一行弹幕的出现次数
save_path = './data.xls'
book.save(save_path)
