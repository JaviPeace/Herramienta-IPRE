class Subject:
    def __init__(self):
        self.observers = []

    def notify(self):
        print("Notification sent")

class Observer:
    def update(self):
        print("Observer updated")
