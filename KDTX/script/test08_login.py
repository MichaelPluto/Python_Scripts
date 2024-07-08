# 导包
from api.login import LoginAPI
# 创建测试类
class TestLoginAPI:
    # 初始化
    uuid = None
    # 前置处理
    def setup_method(self):
        # 实例化对象
        self.login_api = LoginAPI()
        # 获取验证码
        response = self.login_api.get_verify_code()
        print(response.json())
        # 提取验证码接口返回的uuid
        TestLoginAPI.uuid = response.json().get("uuid")


    # 后置处理

    def teardown_method(self):
        pass
    # 登录成功
    def test01_success(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        res = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert 200 == res.status_code
        # 断言响应数据包含 成功
        assert "成功" in res.text
        # 断言响应json数据中code值
        assert 200 == res.json().get("code")

    # 登录失败(用户名为空)
    def test02_without_username(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        res = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert 200 == res.status_code
        # 断言响应数据包含 错误
        assert "错误" in res.text
        # 断言响应json数据中code值
        assert 500 == res.json().get("code")
    # 登录失败(未注册用户)
    def test03_username_not_exsit(self):
        login_data = {
            "username": "jack666",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        res = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert 200 == res.status_code
        # 断言响应数据包含 错误
        assert "错误" in res.text
        # 断言响应json数据中code值
        assert 500 == res.json().get("code")