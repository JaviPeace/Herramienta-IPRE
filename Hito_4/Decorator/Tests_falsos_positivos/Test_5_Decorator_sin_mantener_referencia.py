class Component:
    def run(self):
        pass

class ConcreteComponent(Component):
    def run(self):
        print("ConcreteComponent run")

class Decorator(Component):
    def run(self):
        print("Decorator run")
