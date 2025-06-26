class Singleton:
    instance = None

    def __init__(self):
        if Singleton.instance is not None:
            raise Exception("Ya existe una instancia!")
        Singleton.instance = self

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls()
        return cls.instance

# Uso
a = Singleton.get_instance()
b = Singleton.get_instance()
print(a is b)  # True
