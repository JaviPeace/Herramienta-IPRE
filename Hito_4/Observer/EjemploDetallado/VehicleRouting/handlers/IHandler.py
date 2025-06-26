from abc import ABC, abstractmethod
from typing import List


class IHandler(ABC):
    @abstractmethod
    def set_next(self, next_handler: "IHandler"):
        pass

    @abstractmethod
    def is_solution_valid(self, solution: List[int]) -> bool:
        pass

    @abstractmethod
    def add_subscriber(self, subscriber):
        pass
