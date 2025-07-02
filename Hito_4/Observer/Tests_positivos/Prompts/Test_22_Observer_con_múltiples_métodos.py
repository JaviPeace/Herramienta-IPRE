class Observer:
    def update(self, data):
        print(f"Update with {data}")

    def alert(self, message):
        print(f"Alert: {message}")

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self):
        for obs in self.observers:
            obs.update("data")
            obs.alert("Warning")

s = Subject()
o = Observer()
s.attach(o)
s.notify()
