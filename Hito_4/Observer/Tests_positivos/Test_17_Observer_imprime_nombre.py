class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update()

class NamedObserver:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} notified")

s = Subject()
s.attach(NamedObserver("Observer1"))
s.notify()
