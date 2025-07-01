class Component:
    def send(self, message):
        pass

class User(Component):
    def __init__(self, name):
        self.name = name

    def send(self, message):
        print(f"{self.name} received: {message}")

class Group(Component):
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, component):
        self.members.append(component)

    def send(self, message):
        print(f"Group {self.name} broadcasting: {message}")
        for member in self.members:
            member.send(message)

# Uso
u1 = User("Alice")
u2 = User("Bob")
g = Group("Friends")
g.add(u1)
g.add(u2)
g.send("Hello everyone!")
