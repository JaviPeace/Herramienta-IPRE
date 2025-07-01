class Singleton:
    def __call__(self):
        print("Called")

s = Singleton()
s()
s()
