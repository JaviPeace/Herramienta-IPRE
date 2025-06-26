from component import Notifier

class NotifierDecorator(Notifier):
    def __init__(self, notifier):
        self._notifier = notifier

    def send(self):
        self._notifier.send()

class SMSDecorator(NotifierDecorator):
    def send(self):
        self._notifier.send()
        print("Sending SMS.")

class SlackDecorator(NotifierDecorator):
    def send(self):
        self._notifier.send()
        print("Sending Slack message.")
