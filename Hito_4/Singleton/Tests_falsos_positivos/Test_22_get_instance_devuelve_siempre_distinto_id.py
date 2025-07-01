class Singleton:
    @classmethod
    def get_instance(cls):
        return cls()

print(id(Singleton.get_instance()))
print(id(Singleton.get_instance()))
