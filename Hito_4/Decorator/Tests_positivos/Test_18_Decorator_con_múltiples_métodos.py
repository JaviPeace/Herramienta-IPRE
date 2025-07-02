class Data:
    def load(self):
        print("Loading data")

    def save(self):
        print("Saving data")

class AuditDecorator(Data):
    def __init__(self, data):
        self.data = data

    def load(self):
        print("Audit: before load")
        self.data.load()
        print("Audit: after load")

    def save(self):
        print("Audit: before save")
        self.data.save()
        print("Audit: after save")

d = Data()
audited = AuditDecorator(d)
audited.load()
audited.save()
