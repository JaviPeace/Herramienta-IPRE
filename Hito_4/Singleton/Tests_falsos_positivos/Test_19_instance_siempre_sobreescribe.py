class Singleton:
    instance = None

    @classmethod
    def instance(cls):
        cls.instance = cls()
        return cls.instance

print(Singleton.instance())
print(Singleton.instance())
