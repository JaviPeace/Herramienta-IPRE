class Task:
    def execute(self):
        pass

class SimpleTask(Task):
    def __init__(self, name):
        self.name = name

    def execute(self):
        return f"Executing {self.name}"

class CompositeTask(Task):
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def add(self, task):
        self.subtasks.append(task)

    def execute(self):
        results = [task.execute() for task in self.subtasks]
        return f"Composite Task {self.name}: " + "; ".join(results)

# Uso
task1 = SimpleTask("Download")
task2 = SimpleTask("Unzip")
main = CompositeTask("Install Package")
main.add(task1)
main.add(task2)
print(main.execute())
