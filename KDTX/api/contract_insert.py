import requests
import config


class Contract_InsertAPI:

    def __init__(self):
        self.url = config.BASE_URL + "/api/contract"

    def Contract_Insert(self, test_data, token):
        return requests.post(url=self.url, json=test_data, headers={"Authorization": token})
