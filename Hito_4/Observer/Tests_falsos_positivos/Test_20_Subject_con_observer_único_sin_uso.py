class Subject:
    def __init__(self):
        self.observer = None

    def notify(self):
        print("Notify called")

class Observer:
    def update(self):
        print("Observer updated")
