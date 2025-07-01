class Component:
    def process(self):
        pass

class ConcreteComponent(Component):
    def process(self):
        print("Process ConcreteComponent")

class Decorator(Component):
    def add(self, component):
        print("Decorator add")
