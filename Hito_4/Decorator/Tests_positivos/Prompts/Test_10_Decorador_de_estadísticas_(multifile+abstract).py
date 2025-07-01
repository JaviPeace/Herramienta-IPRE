from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def execute(self): pass

class BasicService(Service):
    def execute(self):
        print("Executing main service")
