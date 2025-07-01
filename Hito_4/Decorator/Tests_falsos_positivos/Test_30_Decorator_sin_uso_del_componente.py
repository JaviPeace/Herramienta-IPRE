class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation")

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        print("Decorator operation")
