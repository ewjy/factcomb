import requests as req
res = req.get('https://news.google.com/topstories?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant') # 指定網址
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
headlines = soup.find_all(name = 'a', attrs = {'class' : 'wEwyrc AVN2gc uQIVzc Sksgp'}) # 抓取頁面中所有標註資訊來源的標籤
source_list = [] # 原始來源list
source_count = {} # 計數後來源dict
for i in headlines:
	source_list.append(i.text) # 將html標籤刪去並放入list
for key in source_list:
	source_count[key] = source_count.get(key, 0) + 1 # 計數並放入dict
print('本次抓取的Google 新聞焦點頁面各來源頻率')
for item, count in source_count.items():
	print('{}：{}'.format(item, count)) # 印出計數結果
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Microsoft JhengHei'] # 指定使用系統內建微軟正黑體以正常顯示中文
plt.rcParams.update({'font.size': 14}) # 字型大小調為14
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
plt.title('本次抓取的Google 新聞焦點頁面各來源頻率', bbox={'facecolor':'0.8', 'pad':5})
plt.pie([float(v) for v in source_count.values()], labels = [str(k) for k in source_count], colors=colors, shadow=True, startangle=140, autopct = '%1.1f%%') # 畫出分佈圓餅圖
plt.show()