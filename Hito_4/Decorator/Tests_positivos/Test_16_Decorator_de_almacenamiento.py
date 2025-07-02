class Storage:
    def save(self):
        print("Saving data")

class BackupDecorator(Storage):
    def __init__(self, storage):
        self.storage = storage

    def save(self):
        self.storage.save()
        print("Creating backup")

s = Storage()
backup_s = BackupDecorator(s)
backup_s.save()
