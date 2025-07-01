class Component:
    def show(self):
        pass

class Leaf(Component):
    def show(self):
        print("Leaf show")

class Composite(Component):
    def __init__(self):
        self.children = {"one": "Leaf1", "two": "Leaf2"}

    def show(self):
        print(self.children)
