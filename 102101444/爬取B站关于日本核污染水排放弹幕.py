from bs4 import BeautifulSoup
import re
import requests

real_list =[]
all_list =[]

#获得搜索页面地址
lst= []
ui = "https://search.bilibili.com/all?keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%9F%93%E6%B0%B4%E6%8E%92%E6%B5%B7&from_source=webtop_search&spm_id_from=333.1007&search_source=5"
lst.append(ui)
for i in range(1,20):
    ui= f"https://search.bilibili.com/all?keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%9F%93%E6%B0%B4%E6%8E%92%E6%B5%B7&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page={i+1}&o={30 * i}"
    lst.append(ui)

for x in range(0,20):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

    }

    url= lst[x]
    #利用requests库获得每个视频BV号
    response = requests.get(url, headers= headers)
    response.encoding='utf-8'
    html = response.text
    web = re.findall(r'(BV.{10})',html)
    all_list.extend(web)
    #去重
    for a in all_list:
        if real_list.count(a)== 0:
            real_list.append(a)
print("爬取的视频数量为：")
print(len(real_list))
for i in real_list[:300]:
    #爬取前300个视频中弹幕的地址
        url1 = f"https://www.bilibili.com/video/{i}/"
        res1 = requests.get(url1, headers=headers)
        res1.encoding = 'utf-8'
        html1 = res1.text
        cid = re.search(r'"cid":(\d*),', html1)
        cid_url = f"https://comment.bilibili.com/{cid}.xml"
        r2 = requests.get(cid_url)
        r2.encoding = 'utf-8'
        soup2 = BeautifulSoup(r2.text, 'html.parser')
        all_barrage = soup2.findAll("d")
        for barrage in all_barrage:
            barrage_string = barrage.string
            #将弹幕存进文本中
            with open('a.txt', 'a', newline='', encoding='utf-8-sig') as file:
                file.write(barrage_string)
                file.write("\n")


