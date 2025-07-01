class Singleton:
    def __new__(cls):
        print("Creating new instance")
        return super().__new__(cls)

s1 = Singleton()
s2 = Singleton()
