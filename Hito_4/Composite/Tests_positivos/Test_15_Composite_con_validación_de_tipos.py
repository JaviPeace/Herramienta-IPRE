class Component:
    def value(self):
        pass

class IntegerLeaf(Component):
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("Must be integer")
        self._value = value

    def value(self):
        return self._value

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        if not isinstance(component, Component):
            raise TypeError("Must be a Component")
        self.children.append(component)

    def value(self):
        return sum(child.value() for child in self.children)

# Uso
leaf1 = IntegerLeaf(3)
leaf2 = IntegerLeaf(7)
comp = Composite()
comp.add(leaf1)
comp.add(leaf2)
print(comp.value())  # 10
