class Subject:
    def attach(self, observer):
        print("Attached observer")

    def notify(self):
        print("Notify observers")

class Observer:
    def update(self):
        print("Observer updated")
