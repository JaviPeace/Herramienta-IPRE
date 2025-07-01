class Singleton:
    created = False

    def __init__(self):
        Singleton.created = True
        print("Created")

s1 = Singleton()
s2 = Singleton()
