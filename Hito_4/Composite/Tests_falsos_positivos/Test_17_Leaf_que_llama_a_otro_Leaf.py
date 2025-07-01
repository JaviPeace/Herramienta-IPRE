class Component:
    def run(self):
        pass

class Leaf(Component):
    def run(self):
        other = Leaf()
        other.run()

class Composite(Component):
    def run(self):
        print("Composite run")
