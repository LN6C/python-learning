import requests
from bs4 import BeautifulSoup
import csv

all_data = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    ' (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}

for page in range(1, 4):
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:#此处异常处理作为网络异常时防止崩溃
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'  # ← 强制 UTF-8，解决 £ 乱码
        
        if response.status_code != 200:
            print(f"第{page}页请求失败，状态码：{response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('article', {'class': 'product_pod'})

        for d in data:
            try:
                bookname_tag = d.find('h3')
                if bookname_tag:
                    a_tag = bookname_tag.find('a')
                    bookname = a_tag['title'] if a_tag else '未知'
                else:
                    bookname = '未知'
                
                price_tag = d.find('p', {'class': 'price_color'})
                price = price_tag.text if price_tag else '未知'
                
                font_tag = d.find('p', {'class': 'instock availability'})
                font = font_tag.text.strip() if font_tag else '未知'
                
                all_data.append({
                    '书籍': bookname,
                    '价格': price,
                    '存量': font
                })
            except Exception as e:
                print(f"解析单条数据出错：{e}")
                continue
        
        print(f"完成第{page}页，本页{len(data)}条")
        
    except requests.exceptions.RequestException as e:
        print(f"网络请求异常：{e}")
        continue
    except Exception as e:
        print(f"其他异常：{e}")
        continue

try:
    with open('无反爬网站基础数据.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['书籍', '价格', '存量'])
        writer.writeheader()
        writer.writerows(all_data)
    print(f"成功保存{len(all_data)}条数据到CSV文件中")
except Exception as e:
    print(f"保存CSV出错:{e}")