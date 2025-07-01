class Component:
    def run(self):
        pass

class ConcreteComponent(Component):
    def run(self):
        print("Run ConcreteComponent")

class Decorator(Component):
    def __init__(self):
        self.children = [1, 2, 3]

    def run(self):
        print("Run Decorator")
