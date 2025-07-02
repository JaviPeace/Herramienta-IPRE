class Counter:
    def count(self):
        return 1

class IncrementDecorator(Counter):
    def __init__(self, counter):
        self.counter = counter

    def count(self):
        return self.counter.count() + 1

c = Counter()
inc_c = IncrementDecorator(c)
print(inc_c.count())
