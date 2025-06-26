class Observer:
    def update(self, msg):
        pass

class Logger(Observer):
    def update(self, msg):
        print(f"Logging: {msg}")

class Alert(Observer):
    def update(self, msg):
        print(f"ALERT: {msg}")

class EventSource:
    def __init__(self):
        self.observers = []

    def add_observer(self, obs):
        self.observers.append(obs)

    def trigger_event(self, msg):
        for obs in self.observers:
            obs.update(msg)

# Uso
source = EventSource()
source.add_observer(Logger())
source.add_observer(Alert())
source.trigger_event("Disk space low")
