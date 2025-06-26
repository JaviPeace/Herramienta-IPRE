class Observer:
    def update(self, event_type, data):
        pass

class ConsoleLogger(Observer):
    def update(self, event_type, data):
        print(f"[{event_type.upper()}] - {data}")

class EventManager:
    def __init__(self):
        self.listeners = {"info": [], "error": []}

    def subscribe(self, event_type, observer):
        self.listeners[event_type].append(observer)

    def notify(self, event_type, data):
        for obs in self.listeners.get(event_type, []):
            obs.update(event_type, data)

# Uso
manager = EventManager()
logger = ConsoleLogger()
manager.subscribe("info", logger)
manager.subscribe("error", logger)

manager.notify("info", "Everything is fine")
manager.notify("error", "Something went wrong")
