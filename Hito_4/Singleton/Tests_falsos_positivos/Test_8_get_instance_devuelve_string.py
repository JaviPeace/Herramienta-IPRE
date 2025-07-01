class Singleton:
    @classmethod
    def get_instance(cls):
        return "singleton"

print(Singleton.get_instance())
