from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import csv

#启动浏览器
service = Service(r"D:\msedgedriver.exe")
driver = webdriver.Edge(service=service)

#准备数据
all_data = []

#爬取第一页和第二页
for page in range(1,3):
    url = f"https://quotes.toscrape.com/page/{page}/"
    driver.get(url)

    #提取所有名言
    quotes = driver.find_elements(By.CSS_SELECTOR,"div.quote")

    for q in quotes:
        text = q.find_element(By.CSS_SELECTOR,"span.text").text
        author = q.find_element(By.CSS_SELECTOR,"small.author").text
        all_data.append({
            '名言':text,
            '作者':author
        })
    print(f"第{page}页完成,共{len(quotes)}条")

#保存csv文件
with open('selenium_quotes.csv','w',encoding='utf-8',newline='')as f:
    writer = csv.DictWriter(f,fieldnames=['名言','作者'])
    writer.writeheader()
    writer.writerows(all_data)
print(f"\n总计保存{len(all_data)}条")

driver.quit()