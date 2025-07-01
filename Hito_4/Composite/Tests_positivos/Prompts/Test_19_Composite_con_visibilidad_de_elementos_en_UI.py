class Component:
    def set_visible(self, visible):
        pass

class Button(Component):
    def __init__(self, label):
        self.label = label
        self.visible = True

    def set_visible(self, visible):
        self.visible = visible
        print(f"Button '{self.label}' visibility set to {visible}")

class Panel(Component):
    def __init__(self):
        self.elements = []

    def add(self, component):
        self.elements.append(component)

    def set_visible(self, visible):
        print(f"Setting visibility for Panel to {visible}")
        for element in self.elements:
            element.set_visible(visible)

# Uso
b1 = Button("Submit")
b2 = Button("Cancel")
panel = Panel()
panel.add(b1)
panel.add(b2)
panel.set_visible(False)
