class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, func):
        self.observers.append(func)

    def notify(self, value):
        for func in self.observers:
            func(value)

def observer_fn(value):
    print(f"Function received: {value}")

s = Subject()
s.attach(observer_fn)
s.notify(100)
