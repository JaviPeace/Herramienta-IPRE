class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def reset(cls):
        cls._instance = None

s1 = Singleton()
Singleton.reset()
s2 = Singleton()
print(s1 is s2)
