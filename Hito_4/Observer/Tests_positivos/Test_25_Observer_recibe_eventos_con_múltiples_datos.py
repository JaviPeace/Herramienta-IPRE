class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, *args, **kwargs):
        for obs in self.observers:
            obs.update(*args, **kwargs)

class Observer:
    def update(self, x, y):
        print(f"Received: {x}, {y}")

s = Subject()
o = Observer()
s.attach(o)
s.notify(10, 20)
