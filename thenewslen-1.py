from bs4 import BeautifulSoup
import requests as req
import numpy as np
import pandas as pd

url="https://www.thenewslens.com/"

res=req.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')

#抓標題
article_title = soup.find_all('h4',attrs={'class':'article-title'})
article_title = [a.find('a').text for a in article_title]

#抓時間
time_tag=soup.find_all('div', attrs={'class':'time'})
time_tag = [t.text for t in time_tag]

#抓分類
categories_tag=soup.find_all('div', attrs={'class':'categories'})
categories_tag=[c.find('a').getText() for c in categories_tag]

#抓作者
authors_tag=soup.find_all('div', attrs={'class':'author'})
authors_tag=[i.find('a').text for i in authors_tag]

for k in range(15):
    print('標題:',article_title[k])
    print('日期:',time_tag[k])
    print('分類:',categories_tag[k])
    print('作者:',authors_tag[k])
    print('=================================================')