class Subject:
    def __init__(self):
        self.observers = 5

    def notify(self):
        print("Notify called")

class Observer:
    def update(self):
        print("Observer updated")
