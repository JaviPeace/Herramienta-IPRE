class Component:
    def send(self):
        pass

class ConcreteComponent(Component):
    def send(self):
        print("ConcreteComponent send")

class Decorator(Component):
    def __init__(self):
        self.component = None

    def send(self):
        print("Decorator send")
