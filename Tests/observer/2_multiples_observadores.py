class Observer:
    def notify(self, value):
        pass

class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, obs):
        self.subscribers.append(obs)

    def broadcast(self, value):
        for sub in self.subscribers:
            sub.notify(value)

class Listener(Observer):
    def notify(self, value):
        print("Got", value)