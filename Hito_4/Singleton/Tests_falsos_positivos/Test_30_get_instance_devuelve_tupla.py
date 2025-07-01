class Singleton:
    @classmethod
    def get_instance(cls):
        return (cls(), cls())

print(Singleton.get_instance())
