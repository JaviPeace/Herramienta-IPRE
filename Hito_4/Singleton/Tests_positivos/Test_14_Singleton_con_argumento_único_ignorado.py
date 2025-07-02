class Singleton:
    _instance = None

    def __new__(cls, value):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = value
        return cls._instance

s1 = Singleton(10)
s2 = Singleton(20)
print(s1.value)
print(s2.value)
