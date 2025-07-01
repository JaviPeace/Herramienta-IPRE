class Singleton:
    def __init__(self):
        print("Instance created")

    @classmethod
    def get_instance(cls):
        return cls()

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
