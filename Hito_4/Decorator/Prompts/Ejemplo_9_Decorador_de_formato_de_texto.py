class Text:
    def render(self):
        return "Hello"

class TextDecorator(Text):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text.render()

class BoldDecorator(TextDecorator):
    def render(self):
        return f"<b>{self._text.render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self):
        return f"<i>{self._text.render()}</i>"

# Uso
plain = Text()
bold = BoldDecorator(plain)
italic_bold = ItalicDecorator(bold)
print(italic_bold.render())  # <i><b>Hello</b></i>
