class Singleton:
    instance = None

    def __init__(self):
        print("Created")

s = Singleton()
