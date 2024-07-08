# 验证登录

import requests

url = "http://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type": "application/json"
}
login_data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": 2,
    "uuid": "437202681b5f4492abfb44472950d3f4"
}
response = requests.post(url=url, headers=header_data, json=login_data)

print(response.status_code)
print(response.json())