class Component:
    def process(self):
        pass

class Leaf(Component):
    def process(self):
        print("Leaf process")

class Composite(Component):
    def process(self):
        print("Composite with no children")
