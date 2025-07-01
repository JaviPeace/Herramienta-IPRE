class Component:
    def render(self):
        pass

class Leaf(Component):
    def __init__(self):
        self.children = []

    def render(self):
        print("Leaf render")

l = Leaf()
l.render()
