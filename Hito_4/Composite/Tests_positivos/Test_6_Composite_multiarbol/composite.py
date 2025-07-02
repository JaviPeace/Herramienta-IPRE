from component import Graphic

class Picture(Graphic):
    def __init__(self):
        self.elements = []

    def add(self, graphic):
        self.elements.append(graphic)

    def draw(self):
        return "Picture with: " + ", ".join(e.draw() for e in self.elements)
