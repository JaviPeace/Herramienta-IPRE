class EventSource:
    def __init__(self):
        self.subscribers = {"click": [], "hover": []}

    def subscribe(self, event, observer):
        self.subscribers[event].append(observer)

    def notify(self, event, data):
        for obs in self.subscribers.get(event, []):
            obs.update(event, data)
