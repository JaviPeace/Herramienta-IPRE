class Singleton:
    count = 0

    def __init__(self):
        Singleton.count += 1
        print(f"Instance {Singleton.count}")

s1 = Singleton()
s2 = Singleton()
