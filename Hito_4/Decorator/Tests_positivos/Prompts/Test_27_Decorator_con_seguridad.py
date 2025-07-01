class API:
    def request(self):
        print("API request")

class AuthDecorator(API):
    def __init__(self, api):
        self.api = api

    def request(self):
        print("Checking authentication")
        self.api.request()

a = API()
auth_a = AuthDecorator(a)
auth_a.request()
