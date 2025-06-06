
class Logger:
    def log(self, msg):
        print("Log:", msg)

class Service:
    def __init__(self):
        self.logger = Logger()

    def execute(self):
        self.logger.log("Running")