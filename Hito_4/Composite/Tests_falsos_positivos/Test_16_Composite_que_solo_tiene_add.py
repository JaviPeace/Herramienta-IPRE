class Component:
    def action(self):
        pass

class Leaf(Component):
    def action(self):
        print("Leaf action")

class Composite(Component):
    def __init__(self):
        pass

    def add(self, component):
        print("Add called")
