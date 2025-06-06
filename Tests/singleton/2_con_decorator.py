def singleton(cls):  # línea 1
    instances = {}  # línea 2
    def wrapper(*args, **kwargs):  # línea 3
        if cls not in instances:  # línea 4
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton  # línea 9
class MySingleton:
    def __init__(self):  # línea 11
        self.value = 42
