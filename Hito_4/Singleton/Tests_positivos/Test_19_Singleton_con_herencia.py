class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class SubSingleton(Singleton):
    pass

s1 = SubSingleton()
s2 = SubSingleton()
print(s1 is s2)
