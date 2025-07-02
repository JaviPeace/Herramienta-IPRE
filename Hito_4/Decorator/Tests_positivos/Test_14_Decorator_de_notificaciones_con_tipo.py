class Notification:
    def send(self):
        print("Base notification")

class EmailDecorator(Notification):
    def __init__(self, notification):
        self.notification = notification

    def send(self):
        self.notification.send()
        print("Sending email notification")

n = Notification()
email_n = EmailDecorator(n)
email_n.send()
