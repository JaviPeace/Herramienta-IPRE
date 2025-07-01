class Singleton:
    @classmethod
    def instance(cls):
        return cls()

print(Singleton.instance())
print(Singleton.instance())
