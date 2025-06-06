class Observer:
    def update(self, data):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, data):
        for obs in self._observers:
            obs.update(data)

class ConcreteObserver(Observer):
    def update(self, data):
        print(f"Received: {data}")