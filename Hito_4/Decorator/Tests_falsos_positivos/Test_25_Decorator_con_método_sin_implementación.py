class Component:
    def operate(self):
        pass

class ConcreteComponent(Component):
    def operate(self):
        print("ConcreteComponent operate")

class Decorator(Component):
    def operate(self):
        pass
