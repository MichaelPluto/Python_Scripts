import json

import pytest

import config
from api.login import LoginAPI
from api.course_insert import Course_InsertAPI


# 读取json文件
def build_data(json_file):
    test_data = []
    with open(json_file, "rb") as f:
        json_data = json.load(f)
        for case in json_data:
            name = case.get("name")
            subject = case.get("subject")
            price = case.get("price")
            application = case.get("application")
            test_data.append((name, subject, price, application))
    return test_data
class TestInsertCourseAPI:
    #初始化
    Token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.insert_coures_api = Course_InsertAPI()

        # 获取验证码
        res_v = self.login_api.get_verify_code()
        # 登录成功
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json().get("uuid")
        }
        res_l = self.login_api.login(login_data)
        # 提取登录token
        TestInsertCourseAPI.Token = res_l.json().get("token")
        print(TestInsertCourseAPI.Token)

    def teardown_method(self):
        pass

    @pytest.mark.parametrize("name, subject, price, application", build_data(config.BASE_PATH + "/data/course.json"))
    def test01_insert_course(self, name, subject, price, application):
        # 课程添加成功
        test_data = {
            "name": name,
            "subject": subject,
            "price": price,
            "application": application
        }
        res = self.insert_coures_api.Course_Insert(test_data, TestInsertCourseAPI.Token)
        print(res.json())
        assert 200 == res.status_code
        assert "操作成功" in res.text
        assert 200 == res.json().get("code")

    def test02_insert_course(self):
        # 课程添加失败
        test_data = {
            "name": "测试开发提升课02",
            "subject": "6",
            "price": 899,
            "application": "2",
            "info": "测试开发提升课02"
        }
        res = self.insert_coures_api.Course_Insert(test_data, "xxx")
        print(res.json())
        assert 200 == res.status_code
        assert "认证失败" in res.text
        assert 401 == res.json().get("code")