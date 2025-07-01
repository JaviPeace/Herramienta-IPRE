class Component:
    def process(self):
        pass

class ConcreteComponent(Component):
    def process(self):
        print("ConcreteComponent process")

class Decorator(Component):
    def __init__(self, component):
        self.other = component

    def decorate(self):
        print("Decorating")
