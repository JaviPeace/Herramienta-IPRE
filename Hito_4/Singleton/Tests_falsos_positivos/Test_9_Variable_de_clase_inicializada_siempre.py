class Singleton:
    instance = "Not an instance"

    def __init__(self):
        print("Created")

s = Singleton()
