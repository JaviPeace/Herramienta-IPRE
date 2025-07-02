class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for obs in self.observers:
            obs.update()

class Observer:
    def update(self):
        print("Notified")

s = Subject()
o = Observer()
s.attach(o)
s.notify()
s.detach(o)
s.notify()
