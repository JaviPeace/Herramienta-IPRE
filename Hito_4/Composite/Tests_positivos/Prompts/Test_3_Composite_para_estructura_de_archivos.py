class FileSystemItem:
    def size(self):
        pass

class File(FileSystemItem):
    def __init__(self, name, size):
        self.name = name
        self._size = size

    def size(self):
        return self._size

class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def size(self):
        return sum(item.size() for item in self.items)

# Uso
file1 = File("file1.txt", 100)
file2 = File("file2.txt", 300)
folder = Folder("docs")
folder.add(file1)
folder.add(file2)
print(folder.size())  # 400
