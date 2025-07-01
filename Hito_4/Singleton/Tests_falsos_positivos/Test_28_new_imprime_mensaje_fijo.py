class Singleton:
    def __new__(cls):
        print("Allocating")
        return super().__new__(cls)

s = Singleton()
