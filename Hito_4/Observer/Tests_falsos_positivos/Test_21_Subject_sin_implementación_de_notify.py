class Subject:
    def attach(self, observer):
        print("Attach called")

class Observer:
    def update(self):
        print("Observer updated")
