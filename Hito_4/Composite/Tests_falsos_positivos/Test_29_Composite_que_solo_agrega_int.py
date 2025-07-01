class Component:
    def add(self, component):
        pass

class Leaf(Component):
    def add(self, component):
        pass

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(1)
