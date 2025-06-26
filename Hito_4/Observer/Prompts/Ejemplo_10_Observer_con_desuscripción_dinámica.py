class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, value):
        print(f"{self.name} recibió: {value}")

class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, obs):
        self._observers.append(obs)

    def unsubscribe(self, obs):
        self._observers.remove(obs)

    def notify(self, value):
        for obs in self._observers[:]:
            obs.update(value)

# Uso
a = Observer("A")
b = Observer("B")
s = Subject()
s.subscribe(a)
s.subscribe(b)
s.notify("Hola")
s.unsubscribe(a)
s.notify("Chao")
