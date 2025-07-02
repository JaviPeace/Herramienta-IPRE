from component import Component

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        print(f"Composite {self.name} operation executed. Propagating to children:")
        for child in self.children:
            child.operation()

