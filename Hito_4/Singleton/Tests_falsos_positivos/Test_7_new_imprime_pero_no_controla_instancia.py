class Singleton:
    def __new__(cls):
        print("New called")
        return super().__new__(cls)

s1 = Singleton()
s2 = Singleton()
