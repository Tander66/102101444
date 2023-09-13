import imageio
import requests
import re
import csv
import jieba
import wordcloud

f = open('B站弹幕.txt',encoding='utf-8')

txt = f.read()
txt_list = jieba.lcut(txt)
string = ' '.join((txt_list))
background =imageio.v2.imread('E:\python\heart.png')
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='C:/Windows/SIMLI.TTF',
                        mask=background,
                        scale=15,
                        contour_width=5,
                        contour_color='red',
                        stopwords={'的','你','我们','了','啊','就','有','是','我','在','喝','不','大','让','和'},
                        )

w.generate(string)
w.to_file('wordcloud.png')
f.close()
