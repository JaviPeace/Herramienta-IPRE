class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update()

class PrintObserver:
    def update(self):
        print("PrintObserver: Notified")

class LogObserver:
    def update(self):
        print("LogObserver: Notified")

s = Subject()
s.attach(PrintObserver())
s.attach(LogObserver())
s.notify()
