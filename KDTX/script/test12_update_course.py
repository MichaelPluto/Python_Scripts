from api.login import LoginAPI
from api.course_update import CourseUpdateAPI

class TestUpdateCourseAPI:
    #初始化
    Token = None

    def setup_method(self):
        self.login_api = LoginAPI()
        self.update_course_api = CourseUpdateAPI()

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
        TestUpdateCourseAPI.Token = res_l.json().get("token")
        print(TestUpdateCourseAPI.Token)

    def teardown_method(self):
        pass

    def test01_update_course(self):

        update_data = {
            "id": 93,
            "name": "接口测试001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍001"
        }
        res = self.update_course_api.Course_Update(update_data, TestUpdateCourseAPI.Token)
        print(res.json())


    def test02_update_course(self):
        pass