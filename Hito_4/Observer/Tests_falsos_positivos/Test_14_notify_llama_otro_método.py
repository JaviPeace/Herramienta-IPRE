class Subject:
    def notify(self):
        self.log()

    def log(self):
        print("Logging notify")

class Observer:
    def update(self):
        print("Observer update")
