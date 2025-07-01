class HTMLElement:
    def render(self):
        pass

class Text(HTMLElement):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class Tag(HTMLElement):
    def __init__(self, tag):
        self.tag = tag
        self.children = []

    def add(self, child):
        self.children.append(child)

    def render(self):
        inner = "".join(child.render() for child in self.children)
        return f"<{self.tag}>{inner}</{self.tag}>"

# Uso
html = Tag("html")
body = Tag("body")
body.add(Text("Hello "))
body.add(Tag("b"))
body.children[1].add(Text("World"))

html.add(body)
print(html.render())
