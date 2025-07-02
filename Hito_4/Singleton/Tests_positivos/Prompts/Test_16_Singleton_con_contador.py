class Singleton:
    _instance = None
    count = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.count += 1
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(Singleton.count)
