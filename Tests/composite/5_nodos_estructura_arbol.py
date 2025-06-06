class Node:  # línea 1
    def __init__(self, name):  # línea 2
        self.name = name
        self.children = []  # línea 4

    def add(self, node):  # línea 6
        self.children.append(node)

    def display(self):  # línea 9
        result = f"Node({self.name})"
        for child in self.children:
            result += "\n  " + child.display()
        return result