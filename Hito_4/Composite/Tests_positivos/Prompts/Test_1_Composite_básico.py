class Component:
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"Leaf {self.name}"

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite {self.name} with children: " + ", ".join(results)

# Uso
root = Composite("root")
root.add(Leaf("A"))
root.add(Leaf("B"))
print(root.operation())
