class Subject:
    def __init__(self):
        self.listeners = []

    def register(self, func):
        self.listeners.append(func)

    def trigger(self, data):
        for f in self.listeners:
            f(data)

def log_event(data):
    print(f"Event: {data}")