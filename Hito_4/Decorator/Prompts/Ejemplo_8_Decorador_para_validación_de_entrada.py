class Processor:
    def process(self, value):
        print(f"Processing {value}")

class ProcessorDecorator(Processor):
    def __init__(self, processor):
        self._processor = processor

    def process(self, value):
        self._processor.process(value)

class ValidationDecorator(ProcessorDecorator):
    def process(self, value):
        if isinstance(value, int) and value >= 0:
            self._processor.process(value)
        else:
            print("Invalid input")

# Uso
processor = Processor()
validated = ValidationDecorator(processor)
validated.process(5)
validated.process(-1)
