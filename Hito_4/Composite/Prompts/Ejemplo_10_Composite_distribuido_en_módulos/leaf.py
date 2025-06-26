from component import Component

class Text(Component):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text
