from collections import Counter
from pyinstrument import Profiler #用于性能分析

profile =Profiler()
profile.start()
f = open('B站弹幕.txt','r',encoding= 'utf-8')
barrage = f.read()
list = barrage.split("\n") #按行分割弹幕
counter = Counter(list) #使用Counter函数对每种弹幕计数
top_20 = counter.most_common(20) #排序出前20出现的弹幕并输出
for item, count in top_20:
    print(item, count)
    with open('弹幕top20.txt', 'a', newline='', encoding='utf-8-sig') as file: #将弹幕及出现次数存入文本
        file.write(item)
        file.write("\n")
        file.write(str(count))
        file.write("\n")
f.close()
profile.stop()
profile.print()