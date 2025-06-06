class FakeSingleton:  # línea 1
    def __init__(self):  # línea 2
        self.value = 0

    def get_instance(self):  # línea 5
        return FakeSingleton()
