class Singleton:
    @classmethod
    def get_instance(cls):
        return cls

print(Singleton.get_instance())
