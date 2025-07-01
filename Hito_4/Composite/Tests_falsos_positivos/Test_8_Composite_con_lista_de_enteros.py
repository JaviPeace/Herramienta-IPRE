class Component:
    def show(self):
        pass

class Leaf(Component):
    def show(self):
        print("Leaf show")

class Composite(Component):
    def __init__(self):
        self.items = [1, 2, 3]

    def show(self):
        print("Composite show")

c = Composite()
c.show()
