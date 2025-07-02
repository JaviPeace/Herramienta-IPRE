from component import Component

class Document(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def render(self):
        return "\n".join(c.render() for c in self.children)
