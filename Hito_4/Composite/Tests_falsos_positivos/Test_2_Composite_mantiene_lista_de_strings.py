class Component:
    def render(self):
        pass

class Leaf(Component):
    def render(self):
        print("Rendering Leaf")

class Composite(Component):
    def __init__(self):
        self.children = ["child1", "child2"]

    def render(self):
        print("Rendering Composite")

c = Composite()
c.render()
