class Manager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def process(self):
        for item in self.items:
            item.run()