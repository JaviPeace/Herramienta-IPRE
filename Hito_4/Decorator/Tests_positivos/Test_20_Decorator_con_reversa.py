class Text:
    def get(self):
        return "Decorator"

class ReverseDecorator(Text):
    def __init__(self, text):
        self.text = text

    def get(self):
        return self.text.get()[::-1]

t = Text()
rev_t = ReverseDecorator(t)
print(rev_t.get())
