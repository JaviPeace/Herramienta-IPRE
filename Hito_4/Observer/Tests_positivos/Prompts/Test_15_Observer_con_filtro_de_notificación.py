class Subject:
    def __init__(self):
        self.observers = []
        self.state = 0

    def attach(self, observer):
        self.observers.append(observer)

    def set_state(self, state):
        self.state = state
        self.notify()

    def notify(self):
        for obs in self.observers:
            obs.update(self.state)

class EvenObserver:
    def update(self, state):
        if state % 2 == 0:
            print(f"EvenObserver: {state}")

s = Subject()
s.attach(EvenObserver())
s.set_state(3)
s.set_state(4)
