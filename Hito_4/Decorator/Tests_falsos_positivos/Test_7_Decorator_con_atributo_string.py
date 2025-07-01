class Component:
    def execute(self):
        pass

class ConcreteComponent(Component):
    def execute(self):
        print("Executing component")

class Decorator(Component):
    def __init__(self):
        self.child = "Not a component"

    def execute(self):
        print("Executing decorator")
