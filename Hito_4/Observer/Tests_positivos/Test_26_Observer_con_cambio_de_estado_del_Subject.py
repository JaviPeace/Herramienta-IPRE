class Subject:
    def __init__(self):
        self.observers = []
        self.state = 0

    def attach(self, obs):
        self.observers.append(obs)

    def change_state(self, state):
        self.state = state
        self.notify()

    def notify(self):
        for obs in self.observers:
            obs.update(self.state)

class Observer:
    def update(self, state):
        print(f"State updated to {state}")

s = Subject()
o = Observer()
s.attach(o)
s.change_state(5)
