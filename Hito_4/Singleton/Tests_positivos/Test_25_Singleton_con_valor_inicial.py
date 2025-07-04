class Counter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.count = 0
        return cls._instance

c = Counter()
c.count += 1
print(c.count)
