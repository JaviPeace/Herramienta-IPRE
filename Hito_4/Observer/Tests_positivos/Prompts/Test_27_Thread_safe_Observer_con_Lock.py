import threading

class Subject:
    def __init__(self):
        self.observers = []
        self.lock = threading.Lock()

    def attach(self, obs):
        with self.lock:
            self.observers.append(obs)

    def notify(self, msg):
        with self.lock:
            for obs in self.observers:
                obs.update(msg)

class Observer:
    def update(self, msg):
        print(f"Thread-safe received: {msg}")

s = Subject()
o = Observer()
s.attach(o)
s.notify("Safe event")
