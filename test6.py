from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# 启动浏览器
service = Service(r"D:\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# 打开网页
driver.get("https://quotes.toscrape.com/")

# 提取第一条名言（新东西）
quote = driver.find_element(By.CSS_SELECTOR, "div.quote span.text")
print("第一条名言：", quote.text)

# 提取第一条作者
author = driver.find_element(By.CSS_SELECTOR, "div.quote small.author")
print("作者：", author.text)

# 关闭浏览器
driver.quit()
#提取元素