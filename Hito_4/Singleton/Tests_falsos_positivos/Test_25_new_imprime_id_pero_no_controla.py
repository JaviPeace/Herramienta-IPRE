class Singleton:
    def __new__(cls):
        obj = super().__new__(cls)
        print(f"Created {id(obj)}")
        return obj

s1 = Singleton()
s2 = Singleton()
