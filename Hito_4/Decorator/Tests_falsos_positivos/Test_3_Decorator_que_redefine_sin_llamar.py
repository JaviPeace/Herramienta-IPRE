class Component:
    def send(self):
        pass

class ConcreteComponent(Component):
    def send(self):
        print("Sending from ConcreteComponent")

class Decorator(Component):
    def send(self):
        print("Sending from Decorator")
