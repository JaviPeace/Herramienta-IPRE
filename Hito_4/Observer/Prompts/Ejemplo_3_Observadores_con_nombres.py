class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, data):
        print(f"{self.name} received {data}")

class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, obs):
        self.subscribers.append(obs)

    def notify_all(self, data):
        for sub in self.subscribers:
            sub.update(data)

# Uso
pub = Publisher()
pub.subscribe(Observer("Obs1"))
pub.subscribe(Observer("Obs2"))
pub.notify_all("event triggered")
