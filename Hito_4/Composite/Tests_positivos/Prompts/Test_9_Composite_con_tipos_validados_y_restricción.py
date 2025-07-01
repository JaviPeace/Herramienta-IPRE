class UIComponent:
    def render(self):
        pass

class Button(UIComponent):
    def render(self):
        return "<button>Click</button>"

class Panel(UIComponent):
    def __init__(self):
        self.children = []

    def add(self, component):
        if not isinstance(component, UIComponent):
            raise ValueError("Invalid component")
        self.children.append(component)

    def render(self):
        return "<panel>" + "".join(c.render() for c in self.children) + "</panel>"

# Uso
p = Panel()
p.add(Button())
# p.add("invalid")  # Esto causaría excepción
print(p.render())
