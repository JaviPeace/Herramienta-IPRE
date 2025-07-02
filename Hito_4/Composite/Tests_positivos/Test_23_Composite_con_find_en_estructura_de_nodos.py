class Component:
    def find(self, name):
        pass

class Employee(Component):
    def __init__(self, name):
        self.name = name

    def find(self, name):
        return self if self.name == name else None

class Department(Component):
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, component):
        self.members.append(component)

    def find(self, name):
        if self.name == name:
            return self
        for member in self.members:
            found = member.find(name)
            if found:
                return found
        return None

# Uso
e1 = Employee("Alice")
e2 = Employee("Bob")
dept = Department("IT")
dept.add(e1)
dept.add(e2)
print(dept.find("Bob").name)  # Bob
