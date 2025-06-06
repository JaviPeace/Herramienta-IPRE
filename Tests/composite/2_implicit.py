class Graphic:  # línea 1
    def draw(self):  # línea 2
        pass

class Circle(Graphic):  # línea 5
    def draw(self):  # línea 6
        return "Circle"

class Group(Graphic):  # línea 9
    def __init__(self):  # línea 10
        self.elements = []

    def add(self, element):  # línea 13
        self.elements.append(element)

    def draw(self):  # línea 16
        return "Group[" + ", ".join(e.draw() for e in self.elements) + "]"
