
import requests
import config
class Contract_UploadAPI:

    def __init__(self):
        self.url = config.BASE_URL + "/api/common/upload"

    def Contract_Upload(self, test_data, token):

        return requests.post(url=self.url, files={"file": test_data}, headers={"Authorization": token})


