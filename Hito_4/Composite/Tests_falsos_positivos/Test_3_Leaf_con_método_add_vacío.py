class Component:
    def add(self, comp):
        pass

class Leaf(Component):
    def add(self, comp):
        pass

    def operation(self):
        print("Leaf op")

leaf = Leaf()
leaf.operation()
