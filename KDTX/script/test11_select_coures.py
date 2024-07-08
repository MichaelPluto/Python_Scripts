from api.login import LoginAPI
from api.course_select import CourseSelectAPI

class TestSelectCourseAPI:
    #初始化
    Token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.select_coures_api = CourseSelectAPI()

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
        TestSelectCourseAPI.Token = res_l.json().get("token")
        print(TestSelectCourseAPI.Token)

    def teardown_method(self):
        pass

    def test01_select_course(self):
        # 查询成功
        res = self.select_coures_api.Select_Course("?name=测试开发提升课01", TestSelectCourseAPI.Token)
        print(res.json())
        assert 200 == res.status_code
        assert "查询成功" in res.text
        assert 200 == res.json().get("code")

    def test02_select_course(self):
        # 查询失败
        res = self.select_coures_api.Select_Course("?name=测试开发提升课01", "xxx")
        print(res.json())
        assert 200 == res.status_code
        assert "认证失败" in res.text
        assert 401 == res.json().get("code")