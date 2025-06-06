class Base:  # línea 1
    def execute(self):  # línea 2
        pass

class SubA(Base):  # línea 5
    def execute(self):  # línea 6
        return "A"

class SubB(Base):  # línea 9
    def execute(self):  # línea 10
        return "B"