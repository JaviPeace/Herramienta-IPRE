class Component:
    def cost(self):
        pass

class Composite(Component):
    def cost(self):
        return 10

class Leaf(Component):
    def __init__(self):
        self.child = Composite()

    def cost(self):
        return self.child.cost()
