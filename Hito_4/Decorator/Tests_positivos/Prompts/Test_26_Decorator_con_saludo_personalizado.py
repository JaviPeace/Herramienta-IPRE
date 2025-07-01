class Greeter:
    def greet(self):
        print("Hello!")

class NameDecorator(Greeter):
    def __init__(self, greeter, name):
        self.greeter = greeter
        self.name = name

    def greet(self):
        self.greeter.greet()
        print(f"Nice to meet you, {self.name}!")

g = Greeter()
named_g = NameDecorator(g, "Alice")
named_g.greet()
