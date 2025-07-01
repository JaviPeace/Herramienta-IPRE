class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        print("Leaf op")

class Composite(Component):
    def operation(self):
        leaf = Leaf()
        leaf.operation()
