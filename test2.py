import requests
from bs4 import BeautifulSoup
import csv
#要爬取的网站
url = "https://quotes.toscrape.com/"
#发送请求
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
#找到所有名言
quotes = soup.find_all('div',class_='quote')
#准备数据
data = []
for q in quotes:
    text = q.find('span',class_='text').text
    author = q.find('small',class_='author').text
    tags = [tag.text for tag in q.find_all('a',class_='tag')]
    data.append({'名言':text,'作者':author,'标签':','.join(tags)})
#保存到csv
with open('quotes.csv','w',newline='',encoding = 'utf-8-sig') as f:
    writer = csv.DictWriter(f,fieldnames=['名言','作者','标签'])
    writer.writeheader()
    writer.writerows(data)
print(f'成功保存{len(data)}条名言到quotes.csv')
#爬取公开页面代码，并保存在csv文件中
