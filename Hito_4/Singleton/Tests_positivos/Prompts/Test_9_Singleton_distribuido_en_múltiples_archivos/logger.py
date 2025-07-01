from singleton import Singleton

class Logger(Singleton):
    def __init__(self):
        self.messages = []

    def log(self, msg):
        self.messages.append(msg)
