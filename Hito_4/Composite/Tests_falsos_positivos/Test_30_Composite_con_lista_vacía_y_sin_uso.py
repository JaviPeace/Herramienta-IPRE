class Component:
    def run(self):
        pass

class Leaf(Component):
    def run(self):
        print("Leaf run")

class Composite(Component):
    def __init__(self):
        self.children = []

    def run(self):
        print("Composite run")
