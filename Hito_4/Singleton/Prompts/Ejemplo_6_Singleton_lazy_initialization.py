class LazySingleton:
    _instance = None

    def __init__(self):
        print("Inicializado")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = LazySingleton()
        return cls._instance

# Uso
print("Antes de llamar a get_instance")
obj = LazySingleton.get_instance()
obj2 = LazySingleton.get_instance()
print(obj is obj2)  # True
