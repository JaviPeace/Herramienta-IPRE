class Component:
    def cost(self):
        pass

class Leaf(Component):
    def cost(self):
        print("Leaf cost")

class Composite(Component):
    def render(self):
        print("Composite render")

leaf = Leaf()
comp = Composite()
leaf.cost()
comp.render()
