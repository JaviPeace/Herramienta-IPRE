class Document:
    def save(self):
        print("Saving document")

class CompressionDecorator(Document):
    def __init__(self, doc):
        self.doc = doc

    def save(self):
        print("Compressing document")
        self.doc.save()

class ValidationDecorator(Document):
    def __init__(self, doc):
        self.doc = doc

    def save(self):
        print("Validating document")
        self.doc.save()

d = Document()
compressed_d = CompressionDecorator(d)
validated_compressed_d = ValidationDecorator(compressed_d)
validated_compressed_d.save()
