class Component:
    def render(self):
        pass

class MenuItem(Component):
    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"MenuItem: {self.name}")

class Menu(Component):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component):
        self.items.append(component)

    def render(self):
        print(f"Menu: {self.name}")
        for item in self.items:
            item.render()

# Uso
file = MenuItem("File")
edit = MenuItem("Edit")
main_menu = Menu("Main Menu")
main_menu.add(file)
main_menu.add(edit)
main_menu.render()
