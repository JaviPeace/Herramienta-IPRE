class Subject:
    def __init__(self):
        self.observers = []
        self.count = 0

    def notify(self):
        self.count += 1
        print(f"Notify count: {self.count}")

class Observer:
    def update(self):
        print("Observer update")
