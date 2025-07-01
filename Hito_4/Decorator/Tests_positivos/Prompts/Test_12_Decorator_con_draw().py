class Shape:
    def draw(self):
        print("Drawing shape")

class BorderDecorator(Shape):
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        self.shape.draw()
        print("Adding border")

s = Shape()
decorated = BorderDecorator(s)
decorated.draw()
