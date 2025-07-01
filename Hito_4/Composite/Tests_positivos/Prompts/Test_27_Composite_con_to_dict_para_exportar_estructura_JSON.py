class Component:
    def to_dict(self):
        pass

class Item(Component):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_dict(self):
        return {self.name: self.value}

class Group(Component):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component):
        self.items.append(component)

    def to_dict(self):
        return {self.name: [item.to_dict() for item in self.items]}

# Uso
i1 = Item("item1", 100)
i2 = Item("item2", 200)
g = Group("group1")
g.add(i1)
g.add(i2)
print(g.to_dict())
