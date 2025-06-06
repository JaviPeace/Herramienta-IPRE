class ObservableValue:
    def __init__(self, initial):
        self._value = initial
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def set(self, value):
        self._value = value
        for obs in self._observers:
            obs(value)