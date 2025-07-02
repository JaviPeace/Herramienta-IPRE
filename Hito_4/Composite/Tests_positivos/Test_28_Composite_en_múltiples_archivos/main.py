from leaf import Leaf
from composite import Composite

if __name__ == "__main__":
    leaf1 = Leaf("A")
    leaf2 = Leaf("B")
    composite = Composite("Root")
    composite.add(leaf1)
    composite.add(leaf2)

    composite.operation()
