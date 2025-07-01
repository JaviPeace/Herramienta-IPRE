class Component:
    def execute(self):
        pass

class ConcreteComponent(Component):
    def execute(self):
        print("ConcreteComponent execute")

class Decorator(Component):
    def __init__(self):
        self.component = 42

    def execute(self):
        print("Decorator execute")
