class Subject:
    def attach(self, observer):
        print("Observer attached")

class Observer:
    def update(self):
        print("Observer updated")

obs = Observer()
subj = Subject()
subj.attach(obs)
