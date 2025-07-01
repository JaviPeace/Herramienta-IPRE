class Component:
    def add(self, component):
        pass

class Leaf(Component):
    def add(self, component):
        print("Leaf add")

class Composite(Component):
    def add(self, component):
        print("Composite add")
