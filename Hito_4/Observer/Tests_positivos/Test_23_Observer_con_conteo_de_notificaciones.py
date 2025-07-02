class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

class Observer:
    def __init__(self):
        self.count = 0

    def update(self, msg):
        self.count += 1
        print(f"Notification {self.count}: {msg}")

s = Subject()
o = Observer()
s.attach(o)
s.notify("Event A")
s.notify("Event B")
