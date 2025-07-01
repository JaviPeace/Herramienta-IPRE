class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

class Observer:
    def update(self):
        print("Observer update")
