class Calculator:
    def calculate(self):
        return 42

class CacheDecorator(Calculator):
    def __init__(self, calculator):
        self.calculator = calculator
        self.cached = None

    def calculate(self):
        if self.cached is None:
            self.cached = self.calculator.calculate()
        return self.cached

c = Calculator()
cached_c = CacheDecorator(c)
print(cached_c.calculate())
print(cached_c.calculate())
