class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf operation")

class Composite(Component):
    def operation(self):
        print("Composite operation")

leaf = Leaf()
comp = Composite()
comp.operation()
