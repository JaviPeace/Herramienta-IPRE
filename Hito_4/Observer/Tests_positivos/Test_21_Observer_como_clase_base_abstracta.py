from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, value):
        pass

class ConcreteObserver(Observer):
    def update(self, value):
        print(f"Received: {value}")

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, value):
        for obs in self.observers:
            obs.update(value)

s = Subject()
o = ConcreteObserver()
s.attach(o)
s.notify(200)
