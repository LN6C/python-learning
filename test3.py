import requests
from bs4 import BeautifulSoup
import csv

all_data = []  # 空列表，存所有页的数据

for page in range(1, 4):  # range(1,4)生成[1,2,3]，爬3页
    
    url = f"https://quotes.toscrape.com/page/{page}/"
    # f-string: {page}会被替换成当前数字
    # 第1次循环: page=1, url=.../page/1/
    # 第2次循环: page=2, url=.../page/2/
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = soup.find_all('div', class_='quote')
    
    for q in quotes:  # 内层循环：处理当前页的每条名言
        text = q.find('span', class_='text').text
        author = q.find('small', class_='author').text
        tags = [tag.text for tag in q.find_all('a', class_='tag')]
        all_data.append({
            '名言': text,
            '作者': author,
            '标签': ', '.join(tags)
        })
    
    print(f"第{page}页爬取完成，共{len(quotes)}条")
    # 每爬完一页，打印进度

# 保存（和test2一样）
with open('quotes_multi.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['名言', '作者', '标签'])
    writer.writeheader()
    writer.writerows(all_data)

print(f"\n总计保存 {len(all_data)} 条名言到 quotes_multi.csv")
#翻页爬取并保存在csv中