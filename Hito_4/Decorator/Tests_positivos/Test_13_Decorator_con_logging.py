class Service:
    def process(self):
        print("Processing data")

class LoggingDecorator(Service):
    def __init__(self, service):
        self.service = service

    def process(self):
        print("Log: Start processing")
        self.service.process()
        print("Log: End processing")

s = Service()
logged_s = LoggingDecorator(s)
logged_s.process()
