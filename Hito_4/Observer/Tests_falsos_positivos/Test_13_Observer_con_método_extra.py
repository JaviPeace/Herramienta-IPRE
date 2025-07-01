class Subject:
    def notify(self):
        print("Notify observers")

class Observer:
    def update(self):
        print("Observer updated")

    def extra(self):
        print("Extra method")
