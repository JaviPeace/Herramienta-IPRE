# Clase base simple y decorador que añade funcionalidad

class Notifier:
    def send(self):
        print("Sending basic notification.")

class NotifierDecorator(Notifier):
    def __init__(self, notifier):
        self._notifier = notifier

    def send(self):
        self._notifier.send()

class EmailDecorator(NotifierDecorator):
    def send(self):
        self._notifier.send()
        print("Sending email notification.")

# Uso
basic = Notifier()
email = EmailDecorator(basic)
email.send()
