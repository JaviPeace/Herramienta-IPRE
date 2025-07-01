class Service:
    def process(self):
        print("Processing")

class AuthDecorator(Service):
    def __init__(self, service):
        self.service = service

    def process(self):
        print("Auth check")
        self.service.process()

class LoggingDecorator(Service):
    def __init__(self, service):
        self.service = service

    def process(self):
        print("Logging start")
        self.service.process()
        print("Logging end")

s = Service()
auth_s = AuthDecorator(s)
logged_auth_s = LoggingDecorator(auth_s)
logged_auth_s.process()
