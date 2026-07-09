import requests
from bs4 import BeautifulSoup
#要爬取的网站网址
url = "https://quotes.toscrape.com/"
#发送请求，获取网页内容
response = requests.get(url)
#用BeautifulSoup4解析网页
soup = BeautifulSoup(response.text,'html.parser')
#提取网页标题
title = soup.find('title').text
#获取第一条名言
quote = soup.find('span',class_ = 'text').text
print("第一条名言",quote)
#提取第一条名言的作者
author = soup.find('small',class_='author').text
print("作者",author)