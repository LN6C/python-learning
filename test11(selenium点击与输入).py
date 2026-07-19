from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

#启动浏览器
service = Service(r"D:\msedgedriver.exe")
driver = webdriver.Edge(service=service)

#打开登录页
driver.get("https://quotes.toscrape.com/login")

#找到用户名输入框，输入文字
username = driver.find_element(By.CSS_SELECTOR,"input[name='username']")
username.send_keys("test")

#找到密码输入框，输入文字
password = driver.find_element(By.CSS_SELECTOR,"input[name='password']")
password.send_keys("test")

#找到登录按钮，点击
login_btn = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
login_btn.click()

#验证登录成功(找logout)
logout = driver.find_element(By.CSS_SELECTOR,"a[href='/logout']")
print("登录成功!"if logout else "登录失败")

driver.quit()
