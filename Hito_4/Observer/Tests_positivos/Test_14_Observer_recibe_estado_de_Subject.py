class Subject:
    def __init__(self):
        self.observers = []
        self.state = None

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update(self.state)

    def set_state(self, state):
        self.state = state
        self.notify()

class Observer:
    def update(self, state):
        print(f"State received: {state}")

s = Subject()
o = Observer()
s.attach(o)
s.set_state("Active")
