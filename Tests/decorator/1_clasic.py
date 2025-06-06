class Component:
    def operation(self):
        raise NotImplementedError

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f"Decorator({self._component.operation()})"
