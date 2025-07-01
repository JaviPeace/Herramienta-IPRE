class Component:
    def display(self):
        pass

class ConcreteComponent(Component):
    def display(self):
        print("ConcreteComponent display")

class Decorator(Component):
    def __init__(self):
        self.child = ConcreteComponent()
