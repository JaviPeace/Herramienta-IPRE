class Subject:
    def notify(self):
        print("Notifying observers")

class Observer:
    def update(self):
        print("Observer updated")
    
    def debug(self):
        print("Debug info")
