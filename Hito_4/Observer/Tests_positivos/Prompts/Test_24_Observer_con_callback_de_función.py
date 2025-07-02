class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, func):
        self.observers.append(func)

    def notify(self, value):
        for func in self.observers:
            func(value)

def print_observer(value):
    print(f"Callback received: {value}")

s = Subject()
s.attach(print_observer)
s.notify(999)
