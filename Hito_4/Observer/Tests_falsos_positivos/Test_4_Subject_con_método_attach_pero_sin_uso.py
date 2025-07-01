class Subject:
    def attach(self, observer):
        self.observer = observer

    def notify(self):
        print("Notifying...")

class Observer:
    def update(self):
        print("Updated")
