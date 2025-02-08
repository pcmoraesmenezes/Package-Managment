import requests

class HandApplication:
    def __init__(self):
        print("HandApplication initialized")
        self.BASE_URL = "https://httpbin.org/get"

    def _get_response(self):
        response = requests.get(self.BASE_URL)
        return response

    def execute(self):
        print("HandApplication executed")
        response = self._get_response()
        print(response.status_code)
        print(response.json())

if __name__ == '__main__':
    app = HandApplication()
    app.execute()
