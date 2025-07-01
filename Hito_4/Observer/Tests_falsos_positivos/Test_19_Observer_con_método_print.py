class Subject:
    def notify(self):
        print("Subject notifying")

class Observer:
    def update(self):
        print("Updating observer")

obs = Observer()
subj = Subject()
subj.notify()
