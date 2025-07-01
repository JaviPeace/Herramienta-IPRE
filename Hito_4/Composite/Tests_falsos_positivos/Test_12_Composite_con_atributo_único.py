class Component:
    def execute(self):
        pass

class Leaf(Component):
    def execute(self):
        print("Leaf executed")

class Composite(Component):
    def __init__(self):
        self.child = Leaf()

    def execute(self):
        self.child.execute()
