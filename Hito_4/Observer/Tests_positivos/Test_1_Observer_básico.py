class Observer:
    def update(self, value):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, value):
        for obs in self.observers:
            obs.update(value)

class PrintObserver(Observer):
    def update(self, value):
        print(f"Received update: {value}")

# Uso
subject = Subject()
observer = PrintObserver()
subject.attach(observer)
subject.notify("Hello")
