class SingletonBase:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBase, cls).__new__(cls)
        return cls._instances[cls]

class Logger(SingletonBase):
    def log(self, message):
        print(message)

class Settings(SingletonBase):
    pass

# Uso
a = Logger()
b = Logger()
c = Settings()
d = Settings()
print(a is b)  # True
print(c is d)  # True
print(a is c)  # False
