class Component:
    def execute(self):
        pass

class Leaf(Component):
    def execute(self):
        print("Leaf execute")

class Composite(Component):
    def __init__(self):
        self.children = [Leaf(), "string"]

    def execute(self):
        print("Composite execute")

comp = Composite()
comp.execute()

