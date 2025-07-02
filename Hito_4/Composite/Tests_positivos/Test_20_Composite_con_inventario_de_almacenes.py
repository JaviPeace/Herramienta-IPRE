class Component:
    def get_quantity(self):
        pass

class Item(Component):
    def __init__(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

class Warehouse(Component):
    def __init__(self):
        self.items = []

    def add(self, component):
        self.items.append(component)

    def get_quantity(self):
        return sum(item.get_quantity() for item in self.items)

# Uso
i1 = Item(100)
i2 = Item(150)
w = Warehouse()
w.add(i1)
w.add(i2)
print(w.get_quantity())  # 250
