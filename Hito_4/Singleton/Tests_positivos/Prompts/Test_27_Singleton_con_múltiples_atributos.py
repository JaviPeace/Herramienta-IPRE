class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.a = 1
            cls._instance.b = 2
        return cls._instance

s = Singleton()
print(s.a, s.b)
