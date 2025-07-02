class Component:
    def get_value(self):
        pass

class Leaf(Component):
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def get_value(self):
        return sum(child.get_value() for child in self.children)

# Uso
leaf1 = Leaf(10)
leaf2 = Leaf(20)
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
print(composite.get_value())  # 30
