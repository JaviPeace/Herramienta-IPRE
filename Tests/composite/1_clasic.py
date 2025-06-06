class Component:  # línea 1
    def operation(self):  # línea 2
        raise NotImplementedError

class Leaf(Component):  # línea 5
    def operation(self):  # línea 6
        return "Leaf"

class Composite(Component):  # línea 9
    def __init__(self):  # línea 10
        self.children = []  # línea 11

    def add(self, component):  # línea 13
        self.children.append(component)

    def operation(self):  # línea 16
        results = [child.operation() for child in self.children]
        return f"Composite({', '.join(results)})"
