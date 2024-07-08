import requests
import config
class Course_InsertAPI:
    def __init__(self):
        self.url = config.BASE_URL +"/api/clues/course"

    def Course_Insert(self, data_json, token):

        return requests.post(url=self.url, json=data_json, headers={"Authorization": token})
