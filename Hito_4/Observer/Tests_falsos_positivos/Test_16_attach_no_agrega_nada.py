class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        pass

    def notify(self):
        print("Notify observers")

class Observer:
    def update(self):
        print("Observer updated")
