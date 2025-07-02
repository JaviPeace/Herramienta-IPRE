# Ejemplo gráfico: decorador para añadir bordes

class Widget:
    def draw(self):
        print("Drawing widget")

class BorderDecorator(Widget):
    def __init__(self, widget):
        self._widget = widget

    def draw(self):
        self._widget.draw()
        print("Adding border")

# Uso
widget = Widget()
decorated = BorderDecorator(widget)
decorated.draw()
