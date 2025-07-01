class Subject:
    def __init__(self):
        self.observers = "Not a list"

    def notify(self):
        print("Notify called")

class Observer:
    def update(self):
        print("Observer updated")
