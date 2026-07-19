import requests
#创建一个Session对象，它会自动管理Cookie
session = requests.Session()
#此网站登录接口为假门，并没有CSRF Token防护
#模拟登录(发送用户名和密码)
login_url = "https://httpbin.org/post" 
login_data = {
    "username":"test_user",
    "password":"test_pass"
} 
#发送post请求
response = session.post(login_url,data=login_data)
print("登录响应状态码:",response.status_code)
print("登录返回内容(前200字):",response.text[:200])

#用一个session访问需要登录的页面
protected_url = "https://httpbin.org/cookie.set/session_id/12345"
response2 = session.get(protected_url)
print("\n访问受保护页面状态码:",response2.status_code)
print("当前Cookie:",session.cookies.get_dict())

#再访问一个页面，验证Cookie还在
response3 = session.get("https://httpbin.org/cookies")
print(response3.json())