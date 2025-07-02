class Component:
    @property
    def size(self):
        pass

class File(Component):
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

class Folder(Component):
    def __init__(self):
        self.contents = []

    def add(self, component):
        self.contents.append(component)

    @property
    def size(self):
        return sum(c.size for c in self.contents)

# Uso
f1 = File(100)
f2 = File(200)
folder = Folder()
folder.add(f1)
folder.add(f2)
print(folder.size)  # 300
