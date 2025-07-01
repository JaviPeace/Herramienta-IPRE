class Subject:
    def notify(self):
        print("Subject notifying")

class Observer:
    def update(self):
        print("Observer updating")

obs = Observer()
subj = Subject()
subj.notify()
