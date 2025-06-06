class SingletonMeta(type):  # línea 1
    _instances = {}  # línea 2

    def __call__(cls, *args, **kwargs):  # línea 3
        if cls not in cls._instances:  # línea 4
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MetaSingleton(metaclass=SingletonMeta):  # línea 9
    def __init__(self):  # línea 10
        self.value = 99
