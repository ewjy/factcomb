import requests as req
domain = input('Enter domain name: ')
res = req.get('https://www.rishavapps.com/hosting-checker/?dmn=' + domain) # 指定網址
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')
fp = open('soup.txt', 'w', encoding="utf-8")
fp.write(str(soup))
fp.close
