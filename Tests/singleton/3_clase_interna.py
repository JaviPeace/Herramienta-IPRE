class Singleton:  # línea 1
    class __Singleton:  # línea 2
        def __init__(self):  # línea 3
            self.value = 42

    _instance = None  # línea 6

    def __new__(cls):  # línea 8
        if not cls._instance:  # línea 9
            cls._instance = cls.__Singleton()
        return cls._instance
