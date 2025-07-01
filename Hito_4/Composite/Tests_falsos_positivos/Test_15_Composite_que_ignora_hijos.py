class Component:
    def process(self):
        pass

class Leaf(Component):
    def process(self):
        print("Leaf process")

class Composite(Component):
    def __init__(self):
        self.children = []

    def process(self):
        print("Composite process")
