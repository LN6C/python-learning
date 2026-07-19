from selenium import webdriver
from selenium.webdriver.edge.service import Service

# 驱动路径
driver_path = r"D:\msedgedriver.exe"

# 创建浏览器对象
service = Service(driver_path)
driver = webdriver.Edge(service=service)

# 打开网页
driver.get("https://quotes.toscrape.com/")

# 提取标题
title = driver.title
print("网页标题：", title)

# 关闭浏览器
driver.quit()
#提取标题