# 导包
import config
from api.login import LoginAPI
from api.course_insert import Course_InsertAPI
from api.contract_upload import Contract_UploadAPI
from api.contract_insert import Contract_InsertAPI
# 测试类
class TestContractBusniess:
    # 初始化
    token = None
    # 文件名
    fileName = None
    # 前置处理
    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.course_api = Course_InsertAPI()
        self.contract_api = Contract_UploadAPI()
        self.contract_Insert_api = Contract_InsertAPI()

    # 后置处理
    def teardown_method(self):
        pass

    # 1、登录成功
    def test01_login_success(self):
        # 获取验证码

        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        print(res_v.json())
        # 打印uuid数据
        print(res_v.json().get("uuid"))

        # 登录
        head_data = {
            "Content-Type": "application/json"
        }

        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": 2,
            "uuid": res_v.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)
        print(res_l.status_code)
        print(res_l.json())

        # 提取登录成功后的token数据，并保存在token属性中
        TestContractBusniess.token = res_l.json().get("token")

    # 2、课程新增成功
    def test02_course_insert(self):
        add_data = {"name": "测试开发提升课01",
                    "subject": "6",
                    "price": 899,
                    "applicablePerson": "2",
                    "info": "测试开发提升课0"
        }

        res = self.course_api.Course_Insert(data_json=add_data, token=TestContractBusniess.token)
        print(res.status_code)
        print(res.json())

    # 3、合同上传成功
    def test03_contract_upload(self):
        # 读取pdf文件
        # f = open("../data/test.pdf", "rb")
        f = open(config.BASE_PATH + "/data/test.pdf", "rb")
        res = self.contract_api.Contract_Upload(test_data=f, token=TestContractBusniess.token)
        print(res.status_code)
        print(res.json())

    # 新增合同成功
    def test04_contract_insert(self):
        # contractNo 唯一
        test_data = { "name": "测试888",
                      "phone": "13612345678",
                      "contractNo": "HT30240629",
                      "subject": "6",
                      "courseId": " 99",
                      "channel": "0",
                      "activityId": 77,
                      "fileName": TestContractBusniess.fileName
        }
        res = self.contract_Insert_api.Contract_Insert(test_data=test_data, token=TestContractBusniess.token)
        print(res.status_code)
        print(res.json())
