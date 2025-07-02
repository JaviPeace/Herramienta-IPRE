class Component:
    def get_score(self):
        pass
    def get_count(self):
        pass

class Student(Component):
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_count(self):
        return 1

class Classroom(Component):
    def __init__(self):
        self.students = []

    def add(self, component):
        self.students.append(component)

    def get_score(self):
        return sum(s.get_score() for s in self.students)

    def get_count(self):
        return sum(s.get_count() for s in self.students)

    def average_score(self):
        return self.get_score() / self.get_count()

# Uso
s1 = Student(80)
s2 = Student(90)
c = Classroom()
c.add(s1)
c.add(s2)
print(c.average_score())  # 85.0
