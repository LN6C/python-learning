from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

service = Service(r"D:\msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("http://quotes.toscrape.com/")

# find_elements 返回列表
quotes = driver.find_elements(By.CSS_SELECTOR, "div.quote")

# 遍历前3个
for i, q in enumerate(quotes[:3], 1):
    # 在 q 里面找名言和作者
    text = q.find_element(By.CSS_SELECTOR, "span.text").text
    author = q.find_element(By.CSS_SELECTOR, "small.author").text
    print(f"{i}. {text} —— {author}")
    
driver.quit()