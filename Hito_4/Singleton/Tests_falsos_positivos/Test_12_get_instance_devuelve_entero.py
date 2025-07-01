class Singleton:
    @staticmethod
    def get_instance():
        return 42

print(Singleton.get_instance())
