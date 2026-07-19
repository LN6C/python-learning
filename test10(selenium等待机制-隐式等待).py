from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import csv

#启动浏览器
service = Service(r"D:\msedgedriver.exe")
driver = webdriver.Edge(service=service)

#隐式等待，找元素，最多10秒
driver.implicitly_wait(10)

#准备数据
all_data = []

#爬取前三页
for page in range(1,4):
    url = f"http://quotes.toscrape.com/page/{page}/"
    driver.get(url)

    #提取所有名言
    quotes = driver.find_elements(By.CSS_SELECTOR,"div.quote")

    for q in quotes:
        text = q.find_element(By.CSS_SELECTOR,"span.text").text
        author = q.find_element(By.CSS_SELECTOR,"small.author").text
        tag_list = q.find_elements(By.CSS_SELECTOR,"a.tag")
        tags = ', '.join([t.text for t in tag_list])

        all_data.append({
            '名言':text,
            '作者':author,
            '标签':tags
        })

    print(f"第{page}页完成,共{len(quotes)}条")

#保存
with open('test10-添加隐式等待机制.csv','w',encoding='utf-8',newline='')as f:
    writer = csv.DictWriter(f,fieldnames=['名言','作者','标签'])
    writer.writeheader()
    writer.writerows(all_data)

print(f"\n总计{len(all_data)}条")

driver.quit()
