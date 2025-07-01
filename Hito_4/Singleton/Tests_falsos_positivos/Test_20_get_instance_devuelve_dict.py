class Singleton:
    @classmethod
    def get_instance(cls):
        return {}

print(Singleton.get_instance())
