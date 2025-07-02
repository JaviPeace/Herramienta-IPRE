from component import Message

class EncryptionDecorator(Message):
    def __init__(self, message):
        self.message = message

    def send(self):
        print("Encrypting message")
        self.message.send()

class LoggingDecorator(Message):
    def __init__(self, message):
        self.message = message

    def send(self):
        print("Logging message")
        self.message.send()
