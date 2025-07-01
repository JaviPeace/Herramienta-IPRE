class Subject:
    def __init__(self):
        self.observers = ["observer1", "observer2"]

    def notify(self):
        print("Notify observers")

class Observer:
    def update(self):
        print("Observer updated")
