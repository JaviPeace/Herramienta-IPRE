class Component:
    def get_depth(self):
        pass

class Leaf(Component):
    def get_depth(self):
        return 1

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def get_depth(self):
        if not self.children:
            return 1
        return 1 + max(child.get_depth() for child in self.children)

# Uso
l = Leaf()
c = Composite()
c2 = Composite()
c.add(l)
c2.add(c)
print(c2.get_depth())  # 3
