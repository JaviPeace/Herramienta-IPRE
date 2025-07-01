class Component:
    def update_status(self, status):
        pass

class Task(Component):
    def __init__(self, name):
        self.name = name
        self.status = "Pending"

    def update_status(self, status):
        self.status = status
        print(f"Task {self.name} status updated to {status}")

class Project(Component):
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add(self, component):
        self.tasks.append(component)

    def update_status(self, status):
        print(f"Updating project {self.name} to {status}")
        for task in self.tasks:
            task.update_status(status)

# Uso
t1 = Task("Write Code")
t2 = Task("Test Code")
p = Project("Development")
p.add(t1)
p.add(t2)
p.update_status("In Progress")
