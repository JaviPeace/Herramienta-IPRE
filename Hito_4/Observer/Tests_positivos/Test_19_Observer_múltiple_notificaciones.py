class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

class Observer:
    def update(self, msg):
        print(f"Notification: {msg}")

s = Subject()
o1 = Observer()
o2 = Observer()
s.attach(o1)
s.attach(o2)
s.notify("First Event")
s.notify("Second Event")
