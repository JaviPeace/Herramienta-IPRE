class Component:
    def operation(self):
        raise NotImplementedError

class Base(Component):
    def operation(self):
        return "Base"

class Wrapper(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return f"Wrapper({self.component.operation()})"

class ExtraWrapper(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return f"Extra({self.component.operation()})"