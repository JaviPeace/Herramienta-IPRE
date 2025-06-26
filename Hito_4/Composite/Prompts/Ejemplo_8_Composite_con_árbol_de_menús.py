class MenuComponent:
    def display(self, indent=0):
        pass

class MenuItem(MenuComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print("  " * indent + f"- {self.name}")

class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def display(self, indent=0):
        print("  " * indent + f"[{self.name}]")
        for item in self.items:
            item.display(indent + 1)

# Uso
file_menu = Menu("File")
file_menu.add(MenuItem("Open"))
file_menu.add(MenuItem("Save"))

edit_menu = Menu("Edit")
edit_menu.add(MenuItem("Cut"))
edit_menu.add(MenuItem("Paste"))

main_menu = Menu("Main")
main_menu.add(file_menu)
main_menu.add(edit_menu)

main_menu.display()
