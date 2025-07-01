class Component:
    def execute(self):
        pass

class ConcreteComponent(Component):
    def execute(self):
        print("ConcreteComponent execute")

class Decorator(Component):
    def perform(self):
        print("Decorator perform")
