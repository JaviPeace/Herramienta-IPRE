class Component:
    def do(self):
        pass

class Leaf(Component):
    def do(self):
        print("Leaf do")

class Composite(Component):
    def do(self):
        print("Composite do")

c = Composite()
c.do
