class Subject:
    def __init__(self):
        self.observers = []

    def notify(self):
        print("Notifying observers")

class Observer:
    def update(self):
        print("Updating observer")
