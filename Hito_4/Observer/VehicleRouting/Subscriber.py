class Subscriber:
    def __init__(self):
        self._status: list[str] = []

    def get_status(self) -> list[str]:
        return self._status

    def update(self, new_status: str):
        self._status.append(new_status)
