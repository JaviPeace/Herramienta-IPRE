class Subject:
    def attach(self, observer):
        pass

    def notify(self):
        print("Notifying observers")

class Observer:
    def update(self):
        print("Observer updated")
