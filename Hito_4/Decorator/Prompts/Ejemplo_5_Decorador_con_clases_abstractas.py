from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def write(self, data): pass

class FileDataSource(DataSource):
    def write(self, data):
        print(f"Writing data: {data}")

class DataSourceDecorator(DataSource):
    def __init__(self, wrappee):
        self._wrappee = wrappee

    def write(self, data):
        self._wrappee.write(data)

class EncryptionDecorator(DataSourceDecorator):
    def write(self, data):
        encrypted = f"[encrypted]{data}[/encrypted]"
        self._wrappee.write(encrypted)

# Uso
source = FileDataSource()
encrypted = EncryptionDecorator(source)
encrypted.write("Sensitive data")
