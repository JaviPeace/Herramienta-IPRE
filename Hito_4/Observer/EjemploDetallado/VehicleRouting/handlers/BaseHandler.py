from IHandler import IHandler


class BaseHandler(IHandler):
    def __init__(self):
        self._next_handler: IHandler | None = None
        self._subscribers: list = []

    def set_next(self, next_handler: IHandler):
        self._next_handler = next_handler

    def is_solution_valid(self, solution: list[int]) -> bool:
        if self._next_handler:
            return self._next_handler.is_solution_valid(solution)
        self.update_subscribers("All good.")
        return True

    def add_subscriber(self, subscriber):
        if self._next_handler:
            self._next_handler.add_subscriber(subscriber)
        self._subscribers.append(subscriber)

    def update_subscribers(self, description: str):
        for subscriber in self._subscribers:
            subscriber.update(description)
