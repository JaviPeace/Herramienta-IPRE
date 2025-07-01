class Product:
    def count(self):
        pass

class Item(Product):
    def __init__(self, name):
        self.name = name

    def count(self):
        return 1

class Box(Product):
    def __init__(self):
        self.contents = []

    def add(self, item):
        self.contents.append(item)

    def count(self):
        return sum(i.count() for i in self.contents)

# Uso
box1 = Box()
box1.add(Item("Book"))
box1.add(Item("Pen"))

box2 = Box()
box2.add(box1)
box2.add(Item("Notebook"))

print(box2.count())  # 3
