class Subject:
    def __init__(self):
        self.observers = []

    def notify(self):
        print("Notify observers")

class Observer:
    def update(self):
        print("Observer update")
