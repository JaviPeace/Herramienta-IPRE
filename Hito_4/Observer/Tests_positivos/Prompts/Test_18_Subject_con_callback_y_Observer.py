class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update("Event Triggered")

class Observer:
    def update(self, message):
        print(f"Observer received: {message}")

s = Subject()
o = Observer()
s.attach(o)
s.notify()
