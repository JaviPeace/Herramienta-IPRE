class Singleton:
    _instance = None

    def __new__(cls, name="default"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
        return cls._instance

s1 = Singleton("first")
s2 = Singleton("second")
print(s1.name)
print(s2.name)
