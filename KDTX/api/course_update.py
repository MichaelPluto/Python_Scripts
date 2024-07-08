import requests
import config
class CourseUpdateAPI:

    def __init__(self):
        self.url = config.BASE_URL +"/api/clues/course"

    def Course_Update(self, test_data, token):
        return requests.put(url=self.url, json=test_data, headers={"Authorization": token})
