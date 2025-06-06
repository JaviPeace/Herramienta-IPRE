class Rule:
    def __init__(self):
        self.warnings = []

    def analyze(self, ast):
        pass

    @classmethod
    def name(cls):
        pass

    def warnings(self):
        return self.warnings