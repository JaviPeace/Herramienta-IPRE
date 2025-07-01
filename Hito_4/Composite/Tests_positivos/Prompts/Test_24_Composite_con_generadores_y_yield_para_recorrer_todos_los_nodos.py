class Component:
    def traverse(self):
        pass

class Leaf(Component):
    def __init__(self, value):
        self.value = value

    def traverse(self):
        yield self.value

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def traverse(self):
        for child in self.children:
            yield from child.traverse()

# Uso
l1 = Leaf(1)
l2 = Leaf(2)
c = Composite()
c.add(l1)
c.add(l2)
print(list(c.traverse()))  # [1, 2]
