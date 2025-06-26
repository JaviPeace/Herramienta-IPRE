class Singleton:
    class _OnlyOne:
        def __init__(self):
            self.value = 42

    _instance = None

    def __new__(cls):
        if not Singleton._instance:
            Singleton._instance = Singleton._OnlyOne()
        return Singleton._instance

# Uso
a = Singleton()
b = Singleton()
print(a is b)  # True
