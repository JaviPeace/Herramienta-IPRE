class Component:
    def render(self):
        pass

class ConcreteComponent(Component):
    def render(self):
        print("ConcreteComponent render")

class Decorator(Component):
    def draw(self):
        print("Decorator draw")
