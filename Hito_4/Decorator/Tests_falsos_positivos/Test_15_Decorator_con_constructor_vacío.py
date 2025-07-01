class Component:
    def send(self):
        pass

class ConcreteComponent(Component):
    def send(self):
        print("ConcreteComponent send")

class Decorator(Component):
    def __init__(self):
        pass

    def send(self):
        print("Decorator send")
