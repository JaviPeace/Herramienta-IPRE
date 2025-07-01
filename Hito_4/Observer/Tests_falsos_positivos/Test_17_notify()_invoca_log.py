class Subject:
    def notify(self):
        self.log()

    def log(self):
        print("Notify logged")

class Observer:
    def update(self):
        print("Observer update")
