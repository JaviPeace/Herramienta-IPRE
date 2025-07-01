class Component:
    def calculate(self):
        pass

class Leaf(Component):
    def calculate(self):
        return 1

class Composite(Component):
    def __init__(self):
        self.child = 5

    def calculate(self):
        return self.child
