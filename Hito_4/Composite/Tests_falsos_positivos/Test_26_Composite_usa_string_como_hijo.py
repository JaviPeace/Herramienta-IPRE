class Component:
    def render(self):
        pass

class Leaf(Component):
    def render(self):
        print("Leaf render")

class Composite(Component):
    def __init__(self):
        self.child = "I am not a component"

    def render(self):
        print(self.child)
