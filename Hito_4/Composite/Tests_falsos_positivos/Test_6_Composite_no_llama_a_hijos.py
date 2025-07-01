class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf working")

class Composite(Component):
    def __init__(self):
        self.children = []

    def operation(self):
        print("Composite doing something")

comp = Composite()
comp.operation()
