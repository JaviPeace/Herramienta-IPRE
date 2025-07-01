class Component:
    def do(self):
        pass

class Leaf(Component):
    def do(self):
        print("Leaf do")

class Composite(Component):
    def __init__(self):
        self.parts = []

    def add(self, component):
        self.parts.append(component)
