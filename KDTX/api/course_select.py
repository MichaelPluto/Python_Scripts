import requests
import config
class CourseSelectAPI:
    # 初始化
    def __init__(self):
        self.url = config.BASE_URL +"/api/clues/list"

    def Select_Course(self, test_data, token):

        return requests.get(url=self.url + f"/{test_data}", headers={"Authorization": token})

