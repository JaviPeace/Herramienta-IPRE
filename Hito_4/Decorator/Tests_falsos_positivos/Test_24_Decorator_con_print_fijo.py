class Component:
    def send(self):
        pass

class ConcreteComponent(Component):
    def send(self):
        print("ConcreteComponent send")

class Decorator(Component):
    def send(self):
        print("Decorator always sends")
