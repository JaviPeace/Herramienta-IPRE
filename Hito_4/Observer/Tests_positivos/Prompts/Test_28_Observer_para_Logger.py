class Logger:
    def update(self, msg):
        print(f"LOG: {msg}")

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, msg):
        for obs in self.observers:
            obs.update(msg)

s = Subject()
l = Logger()
s.attach(l)
s.notify("System started")
