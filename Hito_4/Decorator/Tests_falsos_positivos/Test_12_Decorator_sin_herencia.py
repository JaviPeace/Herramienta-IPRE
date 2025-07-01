class Component:
    def operate(self):
        pass

class ConcreteComponent(Component):
    def operate(self):
        print("Operating ConcreteComponent")

class Decorator:
    def operate(self):
        print("Operating Decorator")
