class Component:
    def render(self):
        pass

class Text(Component):
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content

class Document(Component):
    def __init__(self):
        self.parts = []

    def add(self, component):
        self.parts.append(component)

    def render(self):
        return "\n".join(part.render() for part in self.parts)

# Uso
t1 = Text("Title: Composite Pattern")
t2 = Text("Content: This document explains the composite pattern.")
doc = Document()
doc.add(t1)
doc.add(t2)
print(doc.render())
