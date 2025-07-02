class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.insert(0, obs)

    def notify(self):
        for obs in self.observers:
            obs.update()

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"{self.name} notified")

s = Subject()
s.attach(Observer("Last"))
s.attach(Observer("First"))
s.notify()
