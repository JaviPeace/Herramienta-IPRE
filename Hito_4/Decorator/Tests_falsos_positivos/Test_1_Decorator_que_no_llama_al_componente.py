class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation")

class Decorator(Component):
    def operation(self):
        print("Decorator operation")
