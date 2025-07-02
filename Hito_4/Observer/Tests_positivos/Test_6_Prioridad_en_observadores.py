class Observer:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def update(self, msg):
        print(f"{self.name} received: {msg}")

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)
        self.observers.sort(key=lambda o: o.priority)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

# Uso
a = Observer("A", 2)
b = Observer("B", 1)
s = Subject()
s.attach(a)
s.attach(b)
s.notify("Event happened")  # B primero, luego A
