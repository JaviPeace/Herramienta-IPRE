class Singleton:
    _instance = None
    _value = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

s = Singleton()
s.value = 100
print(s.value)
