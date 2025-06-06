class Warning:
    def __init__(self, name, line, description):
        self.name = name
        self.lineNumber = line
        self.description = description

    def __str__(self):
        return "[ Línea " + str(self.lineNumber) + " ] " + self.name + " - " + self.description

    def __repr__(self):
        return "[ Línea " + str(self.lineNumber) + " ] " + self.name + " - " + self.description

    def __eq__(self, other):
        if isinstance(other, Warning):
            return self.name == other.name and self.lineNumber == other.lineNumber and self.description == other.description
        else:
            return False
        
    def __gt__(self, other):
        if self.lineNumber == other.lineNumber:
            return self.name > other.name
        return self.lineNumber > other.lineNumber