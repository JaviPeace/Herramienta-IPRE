class Node:
    def validate(self):
        pass

    def render(self):
        pass

class Input(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def validate(self):
        return self.value != ""

    def render(self):
        return f"<input name='{self.name}' value='{self.value}'/>"

class Form(Node):
    def __init__(self):
        self.children = []

    def add(self, field):
        self.children.append(field)

    def validate(self):
        return all(child.validate() for child in self.children)

    def render(self):
        return "<form>" + "".join(child.render() for child in self.children) + "</form>"

# Uso
form = Form()
form.add(Input("username", ""))
form.add(Input("email", "example@example.com"))
print(form.validate())  # False
print(form.render())
