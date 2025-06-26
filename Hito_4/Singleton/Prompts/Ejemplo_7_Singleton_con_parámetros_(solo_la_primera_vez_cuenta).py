class Singleton:
    _instance = None

    def __new__(cls, value=None):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.value = value
        return cls._instance

# Uso
a = Singleton("first")
b = Singleton("second")
print(a.value)  # first
print(b.value)  # first
print(a is b)   # True
