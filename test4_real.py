import requests
from bs4 import BeautifulSoup

# 创建 Session
session = requests.Session()

# 第1步：获取登录页面（为了拿到 CSRF token）
login_url = "https://quotes.toscrape.com/login"
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, 'html.parser')

# 查找 CSRF token
token_input = soup.find('input', {'name': 'csrf_token'})
token = token_input['value'] if token_input else None

print("CSRF Token:", token)

# 第2步：提交登录表单
data = {
    'username': 'test',
    'password': 'test',
    'csrf_token': token
}

response = session.post(login_url, data=data)
print("登录提交后状态码:", response.status_code)

# 第3步：访问登录后的页面，验证是否成功
page = session.get("https://quotes.toscrape.com/")
soup2 = BeautifulSoup(page.text, 'html.parser')

# 找 Logout 链接，如果有说明登录成功
logout = soup2.find('a', href='/logout')
if logout:
    print("登录成功！页面里有 Logout 链接")
else:
    print("未找到 Logout，可能登录失败")

# 同时看看有没有欢迎语
welcome = soup2.find(text=lambda t: t and 'Logout' in t)
print("页面内容片段:", soup2.get_text()[:300])