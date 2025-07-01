class Component:
    def area(self):
        pass

class Circle(Component):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Component):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class ShapeGroup(Component):
    def __init__(self):
        self.shapes = []

    def add(self, component):
        self.shapes.append(component)

    def area(self):
        return sum(shape.area() for shape in self.shapes)

# Uso
c = Circle(2)
r = Rectangle(3, 4)
group = ShapeGroup()
group.add(c)
group.add(r)
print(group.area())
