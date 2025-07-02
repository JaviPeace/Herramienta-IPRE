class Component:
    def get_summary(self):
        pass

class Task(Component):
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def get_summary(self):
        return f"{self.name}: {self.hours} hours"

class Project(Component):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component):
        self.items.append(component)

    def get_summary(self):
        summary = f"Project {self.name}:\n"
        for item in self.items:
            summary += "  " + item.get_summary() + "\n"
        return summary.strip()

# Uso
t1 = Task("Write tests", 4)
t2 = Task("Fix bugs", 2)
p = Project("Sprint 1")
p.add(t1)
p.add(t2)
print(p.get_summary())
