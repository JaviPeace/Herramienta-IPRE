class Component:
    CONST = 10

class Leaf:
    def operation(self):
        print("Leaf")

class Composite:
    def operation(self):
        print("Composite")

l = Leaf()
c = Composite()
l.operation()
c.operation()
