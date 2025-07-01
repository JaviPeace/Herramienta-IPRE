class Singleton:
    instance = None

    def __init__(self):
        print("Created")

s1 = Singleton()
s2 = Singleton()
