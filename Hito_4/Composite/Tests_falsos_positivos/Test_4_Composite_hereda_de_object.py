class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf")

class Composite:
    def __init__(self):
        self.children = []

    def operation(self):
        print("Composite")

comp = Composite()
comp.operation()
